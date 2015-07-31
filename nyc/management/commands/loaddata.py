from django.core.management.base import BaseCommand, CommandError
from nyc.models import Person, Bill, Organization, Action
import requests
import json

ocd_jurisdiction_id = 'ocd-jurisdiction/country:us/state:ny/place:new_york/government'
ocd_city_council_id = 'ocd-organization/389257d3-aefe-42df-b3a2-a0d56d0ea731'
base_url = 'http://api.opencivicdata.org'


class Command(BaseCommand):
	help = 'loads in data from the open civic data API'

	def add_arguments(self, parser):
		parser.add_argument('--endpoint', help="a specific endpoint to load data from")

	def handle(self, *args, **options):

		if options['endpoint'] == 'organizations':
			print "\nLOADING ORGANIZATIONS\n"
			self.grab_organizations()
			print "\ndone!"
		elif options['endpoint'] == 'bills':
			print "\nLOADING BILLS\n"
			self.grab_bills()
			print "\ndone!"
		else:
			print "\nLOADING EVERYTHING\n"
			self.grab_organizations()
			self.grab_bills()
			print "\ndone!"


	def grab_organizations(self):

		org_url = base_url+'/organizations/?jurisdiction_id='+ocd_jurisdiction_id
		r = requests.get(org_url)
		page_json = json.loads(r.text)

		for i in range(page_json['meta']['max_page']):

			r = requests.get(org_url+'&page='+str(i+1))
			page_json = json.loads(r.text)

			for result in page_json['results']:
				obj, created = Organization.objects.get_or_create(
						ocd_id=result['id'],
						name=result['name'],
						classification=result['classification']
					)

				if created:
					print '   adding %s' % result['id'] 


	def grab_bills(self):

		bill_url = base_url+'/bills/?from_organization_id='+ocd_city_council_id
		r = requests.get(bill_url)
		page_json = json.loads(r.text)

		for i in range(page_json['meta']['max_page']):

			r = requests.get(bill_url+'&page='+str(i+1))
			page_json = json.loads(r.text)

			for result in page_json['results']:
				self.grab_bill(result['id'])

			break # just grab one page for now

	def grab_bill(self, bill_id):

		bill_url = base_url+'/'+bill_id
		r = requests.get(bill_url)
		page_json = json.loads(r.text)

		from_org = Organization.objects.filter(ocd_id=page_json['from_organization']['id']).first()

		obj, created = Bill.objects.get_or_create(
				ocd_id=bill_id,
				name=page_json['title'],
				classification=page_json['classification'],
				date_created=page_json['created_at'],
				date_updated=page_json['updated_at'],
				source_url=page_json['sources'][0]['url'],
				source_note=page_json['sources'][0]['note'],
				from_organization=from_org
			)

		if created:
			print '   adding %s' % bill_id
		else:
			print '   already exists'

