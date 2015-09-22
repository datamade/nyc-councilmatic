from django.core.management.base import BaseCommand, CommandError
from django.utils.dateparse import parse_datetime, parse_date
from django.utils.text import slugify
from django.db.utils import IntegrityError, DataError
from core.models import Person, Bill, Organization, Action, ActionRelatedEntity, \
						Post, Membership, Sponsorship, LegislativeSession, \
						Document, BillDocument, Event, EventParticipant, EventDocument, \
						EventAgendaItem, AgendaItemBill
from councilmatic.settings import HEADSHOT_PATH, DEBUG
from councilmatic.city_config import OCD_JURISDICTION_ID, OCD_CITY_COUNCIL_ID, TIMEZONE
import requests
import json
import pytz
import os.path
import re

app_timezone = pytz.timezone(TIMEZONE)
base_url = 'http://ocd.datamade.us'

class Command(BaseCommand):
	help = 'loads in data from the open civic data API'

	def add_arguments(self, parser):
		parser.add_argument('--endpoint', help="a specific endpoint to load data from")
		
		parser.add_argument('--delete',
            action='store_true',
            default=False,
            help='delete data before loading')

	def handle(self, *args, **options):

		if options['endpoint'] == 'organizations':
			print("\nLOADING ORGANIZATIONS\n")
			self.grab_organizations(delete=options['delete'])
			print("\ndone!")
		elif options['endpoint'] == 'bills':
			print("\nLOADING BILLS\n")
			self.grab_bills(delete=options['delete'])
			print("\ndone!")
		elif options['endpoint'] == 'people':
			print("\nLOADING PEOPLE\n")
			self.grab_people(delete=options['delete'])
			print("\ndone!")
		elif options['endpoint'] == 'events':
			print("\nLOADING EVENTS\n")
			self.grab_events(delete=options['delete'])
		else:
			print("\nLOADING EVERYTHING\n")
			self.grab_organizations(delete=options['delete'])
			self.grab_bills(delete=options['delete'])
			self.grab_people(delete=options['delete'])
			self.grab_events(delete=options['delete'])
			print("\ndone!")
		
	def grab_organizations(self, delete=False):

		if delete:
			print("deleting all organizations and posts")
			Organization.objects.all().delete()
			Post.objects.all().delete()

		# first grab ny city council root
		self.grab_organization_posts(OCD_CITY_COUNCIL_ID)

		# this grabs a paginated listing of all organizations within a jurisdiction
		orgs_url = base_url+'/organizations/?jurisdiction_id='+OCD_JURISDICTION_ID
		r = requests.get(orgs_url)
		page_json = json.loads(r.text)

		for i in range(page_json['meta']['max_page']):

			r = requests.get(orgs_url+'&page='+str(i+1))
			page_json = json.loads(r.text)

			for result in page_json['results']:

				self.grab_organization_posts(result['id'])


	def grab_organization_posts(self, organization_ocd_id, parent=None):

		url = base_url+'/'+organization_ocd_id
		r = requests.get(url)
		page_json = json.loads(r.text)

		if parent:
			try:
				org_obj, created = Organization.objects.get_or_create(
						ocd_id=organization_ocd_id,
						name=page_json['name'],
						classification=page_json['classification'],
						slug=slugify(page_json['name']),
						parent=parent,
					)
			except IntegrityError:
				ocd_id_part = organization_ocd_id.rsplit('-',1)[1]
				org_obj, created = Organization.objects.get_or_create(
						ocd_id=organization_ocd_id,
						name=page_json['name'],
						classification=page_json['classification'],
						slug=slugify(page_json['name'])+ocd_id_part,
						parent=parent,
					)
		else:
			try:
				org_obj, created = Organization.objects.get_or_create(
						ocd_id=organization_ocd_id,
						name=page_json['name'],
						classification=page_json['classification'],
						slug=slugify(page_json['name']),
					)
			except IntegrityError:
				ocd_id_part = organization_ocd_id.rsplit('-',1)[1]
				org_obj, created = Organization.objects.get_or_create(
						ocd_id=organization_ocd_id,
						name=page_json['name'],
						classification=page_json['classification'],
						slug=slugify(page_json['name'])+ocd_id_part,
					)

		if created and DEBUG:
			print('   adding organization: %s' % org_obj.name )

		for post_json in page_json['posts']:

			obj, created = Post.objects.get_or_create(
					ocd_id = post_json['id'],
					label = post_json['label'],
					role = post_json['role'],
					organization = org_obj,
				)

			if created and DEBUG:
				print('      adding post: %s %s' %(post_json['role'], post_json['label']))

		for child in page_json['children']:
			self.grab_organization_posts(child['id'], org_obj)


	def grab_people(self, delete=False):
		# find people associated with existing organizations & bills

		if delete:
			print("deleting all people, memberships, sponsorships")
			Person.objects.all().delete()
			Membership.objects.all().delete()
			Sponsorship.objects.all().delete()

		# grab people associated with all existing organizations
		orgs = Organization.objects.exclude(name='Democratic').exclude(name='Republican').all()
		for organization in orgs:
			url = base_url+'/'+organization.ocd_id
			r = requests.get(url)
			page_json = json.loads(r.text)

			for membership_json in page_json['memberships']:
				self.grab_person_memberships(membership_json['person']['id'])

		# add sponsorships for all existing bills
		bills = Bill.objects.all()
		for bill in bills:
			url = base_url+'/'+bill.ocd_id
			r = requests.get(url)
			page_json = json.loads(r.text)

			for sponsor_json in page_json['sponsorships']:
				sponsor=Person.objects.filter(ocd_id=sponsor_json['entity_id']).first()
				if sponsor:
					obj, created = Sponsorship.objects.get_or_create(
							bill=bill,
							person=sponsor,
							classification=sponsor_json['classification'],
							is_primary=sponsor_json['primary'],
						)

					if created and DEBUG:
						print('      adding sponsorship: %s %s' % (obj.bill, obj.person))
	

	def grab_bills(self, delete=False):
		# this grabs all bills & associated actions, documents from city council
		# organizations need to be populated before bills & actions are populated
		
		if delete:
			print("deleting all bills, actions, legislative sessions")
			Bill.objects.all().delete()
			Action.objects.all().delete()
			ActionRelatedEntity.objects.all().delete()
			LegislativeSession.objects.all().delete()
			Document.objects.all().delete()
			BillDocument.objects.all().delete()

		# get legislative sessions
		self.grab_legislative_sessions()

		bill_url = base_url+'/bills/?from_organization_id='+OCD_CITY_COUNCIL_ID
		r = requests.get(bill_url)
		page_json = json.loads(r.text)

		for i in range(page_json['meta']['max_page']):

			r = requests.get(bill_url+'&page='+str(i+1))
			page_json = json.loads(r.text)

			for result in page_json['results']:
				self.grab_bill(result['id'])

	def grab_legislative_sessions(self):

		# TO-DO: update this when ocd data is fixed
		obj, created = LegislativeSession.objects.get_or_create(
				identifier='2014',
				jurisdiction_ocd_id=OCD_JURISDICTION_ID,
				name='2014 Legislative Session',
			)
		if created and DEBUG:
			print('adding legislative session: %s' %obj.name)

	def grab_bill(self, bill_id):

		bill_url = base_url+'/'+bill_id
		r = requests.get(bill_url)
		page_json = json.loads(r.text)

		from_org = Organization.objects.filter(ocd_id=page_json['from_organization']['id']).first()
		legislative_session = LegislativeSession.objects.filter(identifier=page_json['legislative_session']['identifier']).first()

		# THIS IF STATEMENT IS A NYC CUSTOMIZATION
		# only load bills that have a local classification
		# this is a temporary fix - remove when outdated bills are no longer in ocd
		if 'local_classification' in page_json['extras']:
			bill_type = page_json['extras']['local_classification']

			if 'full_text' in page_json['extras']:
				full_text = page_json['extras']['full_text']
			else:
				full_text = ''

			if page_json['abstracts']:
				abstract = page_json['abstracts'][0]['abstract']
			else:
				abstract = ''

			try:
				obj, created = Bill.objects.get_or_create(
						ocd_id=bill_id,
						description=page_json['title'],
						identifier=page_json['identifier'],
						classification=page_json['classification'][0],
						date_created=page_json['created_at'],
						date_updated=page_json['updated_at'],
						source_url=page_json['sources'][0]['url'],
						source_note=page_json['sources'][0]['note'],
						from_organization=from_org,
						full_text=full_text,
						abstract=abstract,
						legislative_session=legislative_session,
						bill_type=bill_type,
						slug=slugify(page_json['identifier']),
					)
			except IntegrityError:
				ocd_id_part = bill_id.rsplit('-',1)[1]
				obj, created = Bill.objects.get_or_create(
						ocd_id=bill_id,
						description=page_json['title'],
						identifier=page_json['identifier'],
						classification=page_json['classification'][0],
						date_created=page_json['created_at'],
						date_updated=page_json['updated_at'],
						source_url=page_json['sources'][0]['url'],
						source_note=page_json['sources'][0]['note'],
						from_organization=from_org,
						full_text=full_text,
						abstract=abstract,
						legislative_session=legislative_session,
						bill_type=bill_type,
						slug=slugify(page_json['identifier'])+ocd_id_part,
					)

			if created and DEBUG:
				print('   adding %s' % bill_id)

			action_order = 0
			for action_json in page_json['actions']:
				self.load_action(action_json, obj, action_order)
				action_order+=1

			# update bill last_action_date with most recent action
			obj.last_action_date = obj.get_last_action_date()
			obj.save()

			# update documents associated with a bill
			for document_json in page_json['documents']:
				self.load_bill_document(document_json, obj)

		# if bills don't have local classification, don't load them
		else:
			print("*"*60)
			print("SKIPPING BILL %s" %bill_id)
			print("bill data looks incomplete")
			print("*"*60)


	def load_action(self, action_json, bill, action_order):

		org = Organization.objects.filter(ocd_id=action_json['organization']['id']).first()

		classification = ""
		if action_json['classification']:
			classification = action_json['classification'][0]

		action_obj, created = Action.objects.get_or_create(
				date=action_json['date'],
				classification=classification,
				description=action_json['description'],
				organization=org,
				bill=bill,
				order=action_order,
			)

		if created and DEBUG:
			print('      adding action: %s' %action_json['description'])

		for related_entity_json in action_json['related_entities']:
			obj, created = ActionRelatedEntity.objects.get_or_create(
				action = action_obj,
				entity_type = related_entity_json['entity_type'],
				entity_name = related_entity_json['name'],
				organization_ocd_id = related_entity_json['organization_id'] if related_entity_json['organization_id'] else "",
				person_ocd_id = related_entity_json['person_id'] if related_entity_json['person_id'] else ""
			)

			if created and DEBUG:
				print('         adding related entity: %s' %obj.entity_name)

	def load_bill_document(self, document_json, bill):

		doc_obj, created = Document.objects.get_or_create(
				note=document_json['note'],
				url=document_json['links'][0]['url'],
			)

		obj, created = BillDocument.objects.get_or_create(
				bill = bill,
				document = doc_obj,
			)

		if created:
			print('      adding document: %s' % doc_obj.note)


	def grab_person_memberships(self, person_id):
		# this grabs a person and all their memberships

		url = base_url+'/'+person_id
		r = requests.get(url)
		page_json = json.loads(r.text)

		# TO DO: handle updating people & memberships
		person = Person.objects.filter(ocd_id=person_id).first()
		if not person:

			# save image to disk
			if page_json['image']:
				print("   saving image for %s" % page_json['name'])
				r = requests.get(page_json['image'])
				if r.status_code == 200:
				    with open((HEADSHOT_PATH + page_json['id'] + ".jpg"), 'wb') as f:
				        for chunk in r.iter_content(1000):
        					f.write(chunk)

			email = ''
			for contact_detail in page_json['contact_details']:
				if contact_detail['type'] == 'email':
					if contact_detail['value'] != 'mailto:':
						email = contact_detail['value']

			website_url = ''
			for link in page_json['links']:
				if link['note'] == "web site":
					website_url = link['url']


			try:
				person = Person.objects.create(
					ocd_id=page_json['id'],
					name=page_json['name'],
					headshot=page_json['image'],
					source_url=page_json['sources'][0]['url'],
					source_note=page_json['sources'][0]['note'],
					website_url = website_url,
					email = email,
					slug=slugify(page_json['name']),
				)
			except IntegrityError:
				ocd_id_part=page_json['id'].rsplit('-',1)[1]
				person = Person.objects.create(
					ocd_id=page_json['id'],
					name=page_json['name'],
					headshot=page_json['image'],
					source_url=page_json['sources'][0]['url'],
					source_note=page_json['sources'][0]['note'],
					website_url = '',
					email = email,
					slug=slugify(page_json['name'])+ocd_id_part,
				)

			if DEBUG:
				print('   adding person: %s' % person.name)

		for membership_json in page_json['memberships']:

			if membership_json['post']:
				post = Post.objects.filter(ocd_id=membership_json['post']['id']).first()
			else:
				post = None

			organization = Organization.objects.filter(ocd_id=membership_json['organization']['id']).first()
			# adding republican or democratic party when encountered
			# b/c parties are not added when organizations are loaded (in grab_organizations)
			if not organization and membership_json['organization']['name'] in ['Republican', 'Democratic']:
				self.grab_organization_posts(membership_json['organization']['id'])
				organization = Organization.objects.filter(ocd_id=membership_json['organization']['id']).first()

			try:
				end_date = parse_date(membership_json['end_date'])
			except:
				end_date = None
			try:
				start_date = parse_date(membership_json['start_date'])
			except:
				start_date = None

			obj, created = Membership.objects.get_or_create(
					organization = organization,
					person = person,
					post = post,
					label = membership_json['label'],
					role = membership_json['role'],
					start_date = start_date,
					end_date = end_date
				)

			if created and DEBUG:
				print('      adding membership: %s' % obj.role)

	def grab_events(self, delete=False):

		if delete:
			print("deleting all events")
			Event.objects.all().delete()
			EventParticipant.objects.all().delete()
			EventDocument.objects.all().delete()
			EventAgendaItem.objects.all().delete()
			AgendaItemBill.objects.all().delete()

		# this grabs a paginated listing of all events within a jurisdiction
		events_url = base_url+'/events/?jurisdiction_id='+OCD_JURISDICTION_ID
		r = requests.get(events_url)
		page_json = json.loads(r.text)

		for i in range(page_json['meta']['max_page']):

			r = requests.get(events_url+'&page='+str(i+1))
			page_json = json.loads(r.text)

			for result in page_json['results']:
				self.grab_event(result['id'])

	def grab_event(self, event_ocd_id):

		event_url = base_url+'/'+event_ocd_id
		r = requests.get(event_url)


		if r.status_code == 200:
			page_json = json.loads(r.text)

			try:
				legistar_id = re.findall('ID=(.*)&GUID', page_json['sources'][0]['url'])[0]
				event_obj, created = Event.objects.get_or_create(
						ocd_id = event_ocd_id,
						name = page_json['name'],
						description = page_json['description'],
						classification = page_json['classification'],
						start_time = parse_datetime(page_json['start_time']),
						end_time = parse_datetime(page_json['end_time']) if page_json['end_time'] else None,
						all_day = page_json['all_day'],
						status = page_json['status'],
						location_name = page_json['location']['name'],
						location_url = page_json['location']['url'],
						source_url = page_json['sources'][0]['url'],
						source_note = page_json['sources'][0]['note'],
						slug = legistar_id,
					)

				if created and DEBUG:
					print('   adding event: %s' % event_ocd_id)

				for participant_json in page_json['participants']:
					obj, created = EventParticipant.objects.get_or_create(
							event = event_obj,
							note = participant_json['note'],
							entity_name = participant_json['entity_name'],
							entity_type = participant_json['entity_type']
						)
					if created and DEBUG:
						print('      adding participant: %s' %obj.entity_name)

				for document_json in page_json['documents']:
					self.load_eventdocument(document_json, event_obj)

				for agenda_item_json in page_json['agenda']:
					self.load_eventagendaitem(agenda_item_json, event_obj)

			# TEMPORARY - skip events w/ names that are too long
			# this will be fixed when names no longer have descriptions appended
			except DataError:
				print("*"*60)
				print("SKIPPING EVENT %s" %event_ocd_id)
				print("error loading event data")
				print("*"*60)

		else:
			print("*"*60)
			print("SKIPPING EVENT %s" %event_ocd_id)
			print("cannot retrieve event data")
			print("*"*60)

	def load_eventagendaitem(self, agenda_item_json, event):

		agendaitem_obj, created = EventAgendaItem.objects.get_or_create(
				event = event,
				order = agenda_item_json['order'],
				description = agenda_item_json['description'],
			)

		if created and DEBUG:
			print('      adding agenda item: %s' %agendaitem_obj.order)

		related_entity_json = agenda_item_json['related_entities'][0]
		clean_bill_identifier = re.sub(' 0', ' ', related_entity_json['entity_name'])
		related_bill = Bill.objects.filter(identifier = clean_bill_identifier).first()

		if related_bill:
			obj, created = AgendaItemBill.objects.get_or_create(
					agenda_item = agendaitem_obj,
					bill = related_bill,
					note = related_entity_json['note'],
				)

			if created and DEBUG:
				print('         adding related bill: %s' %related_bill.identifier)


	def load_eventdocument(self, document_json, event):

		doc_obj, created = Document.objects.get_or_create(
				note=document_json['note'],
				url=document_json['links'][0]['url'],
			)

		obj, created = EventDocument.objects.get_or_create(
				event = event,
				document = doc_obj,
			)

		if created and DEBUG:
			print('      adding document: %s' % doc_obj.note)
