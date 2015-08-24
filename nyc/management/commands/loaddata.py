from django.core.management.base import BaseCommand, CommandError
from django.utils.dateparse import parse_datetime, parse_date
from django.utils.text import slugify
from django.db.utils import IntegrityError
from nyc.models import Person, Bill, Organization, Action, Post, Membership
from councilmatic.settings import HEADSHOT_PATH
import requests
import json
import pytz
import os.path

ocd_jurisdiction_id = 'ocd-jurisdiction/country:us/state:ny/place:new_york/government'
ocd_city_council_id = 'ocd-organization/389257d3-aefe-42df-b3a2-a0d56d0ea731'
base_url = 'http://api.opencivicdata.org'
eastern = pytz.timezone('US/Eastern')


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
		else:
			print("\nLOADING EVERYTHING\n")
			self.grab_organizations(delete=options['delete'])
			self.grab_bills(delete=options['delete'])
			self.grab_people(delete=options['delete'])
			print("\ndone!")
		
	def grab_organizations(self, delete=False):

		if delete:
			print("deleting all organizations and posts")
			Organization.objects.all().delete()
			Post.objects.all().delete()

		# first grab ny city council root
		self.grab_organization_posts(ocd_city_council_id)

		# this grabs all organizations within a jurisdiction
		orgs_url = base_url+'/organizations/?jurisdiction_id='+ocd_jurisdiction_id
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

		if created:
			print('   adding organization: %s' % org_obj.name )

		for post_json in page_json['posts']:

			obj, created = Post.objects.get_or_create(
					ocd_id = post_json['id'],
					label = post_json['label'],
					role = post_json['role'],
					organization = org_obj,
				)

			if created:
				print('      adding post: %s %s' %(post_json['role'], post_json['label']))

		for child in page_json['children']:
			self.grab_organization_posts(child['id'], org_obj)


	def grab_people(self, delete=False):
		# find people associated with existing organizations

		if delete:
			print("deleting all people and memberships")
			Person.objects.all().delete()
			Membership.objects.all().delete()

		orgs = Organization.objects.all()

		for organization in orgs:
			url = base_url+'/'+organization.ocd_id
			r = requests.get(url)
			page_json = json.loads(r.text)

			for membership_json in page_json['memberships']:

				self.grab_person_memberships(membership_json['person']['id'])


	def grab_bills(self, delete=False):
		# this grabs all bills & associated actions from city council
		# organizations need to be populated before bills & actions are populated
		
		if delete:
			print("deleting all bills and actions")
			Bill.objects.all().delete()
			Action.objects.all().delete()

		bill_url = base_url+'/bills/?from_organization_id='+ocd_city_council_id
		r = requests.get(bill_url)
		page_json = json.loads(r.text)

		for i in range(page_json['meta']['max_page']):

			r = requests.get(bill_url+'&page='+str(i+1))
			page_json = json.loads(r.text)

			for result in page_json['results']:
				self.grab_bill(result['id'])

	def grab_bill(self, bill_id):

		bill_url = base_url+'/'+bill_id
		r = requests.get(bill_url)
		page_json = json.loads(r.text)

		from_org = Organization.objects.filter(ocd_id=page_json['from_organization']['id']).first()

		try:
			obj, created = Bill.objects.get_or_create(
					ocd_id=bill_id,
					name=page_json['title'],
					identifier=page_json['identifier'],
					classification=page_json['classification'][0],
					date_created=page_json['created_at'],
					date_updated=page_json['updated_at'],
					source_url=page_json['sources'][0]['url'],
					source_note=page_json['sources'][0]['note'],
					from_organization=from_org,
					slug=slugify(page_json['identifier']),
				)
		except IntegrityError:
			ocd_id_part = bill_id.rsplit('-',1)[1]
			obj, created = Bill.objects.get_or_create(
					ocd_id=bill_id,
					name=page_json['title'],
					identifier=page_json['identifier'],
					classification=page_json['classification'][0],
					date_created=page_json['created_at'],
					date_updated=page_json['updated_at'],
					source_url=page_json['sources'][0]['url'],
					source_note=page_json['sources'][0]['note'],
					from_organization=from_org,
					slug=slugify(page_json['identifier'])+ocd_id_part,
				)

		if created:
			print('   adding %s' % bill_id)

		for action_json in page_json['actions']:
			self.load_action(action_json, obj)

	def load_action(self, action_json, bill):

		org = Organization.objects.filter(ocd_id=action_json['organization']['id']).first()

		obj, created = Action.objects.get_or_create(
				date=action_json['date'],
				classification=action_json['classification'],
				description=action_json['description'],
				organization=org,
				bill=bill,
			)

		if created:
			print('      adding action: %s' %action_json['description'])

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
				print("saving image for %s" % page_json['name'])
				r = requests.get(page_json['image'])
				if r.status_code == 200:
				    with open((HEADSHOT_PATH + page_json['id'] + ".jpg"), 'wb') as f:
				        for chunk in r.iter_content(1000):
        					f.write(chunk)

			try:
				person = Person.objects.create(
					ocd_id=page_json['id'],
					name=page_json['name'],
					headshot=page_json['image'],
					source_url=page_json['sources'][0]['url'],
					source_note=page_json['sources'][0]['note'],
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
					slug=slugify(page_json['name'])+ocd_id_part,
				)

			print('      adding person: %s' % person.name)

		for membership_json in page_json['memberships']:

			if membership_json['post']:
				post = Post.objects.filter(ocd_id=membership_json['post']['id']).first()
			else:
				post = None

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

			if created:
				print('      adding membership: %s' % obj.role)
