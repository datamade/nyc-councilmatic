from django.core.management.base import BaseCommand, CommandError
from nyc.models import Person, Bill, Organization, Action
import requests
import json

ocd_jurisdiction_id = 'ocd-jurisdiction/country:us/state:ny/place:new_york/government'
base_url = 'http://api.opencivicdata.org'


class Command(BaseCommand):
	help = 'loads in data from the open civic data API'

	def add_arguments(self, parser):
		parser.add_argument('--endpoint', help="a specific endpoint to load data from")

	def handle(self, *args, **options):

		if options['endpoint'] == 'organizations':
			print "\nLOADING ORGANIZATIONS\n"
			grab_organizations()
			print "\ndone!"
		elif options['endpoint'] == 'bills':
			print "\nLOADING BILLS\n"
			grab_bills()
			print "\ndone!"
		else:
			print "\nLOADING EVERYTHING\n"
			grab_organizations()
			grab_bills()
			print "\ndone!"


def grab_organizations():

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


def grab_bills():

	bill_url = base_url

