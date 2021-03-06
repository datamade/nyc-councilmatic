from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from councilmatic_core.models import Organization, Person
from nyc.models import NYCBill

class BillDetailViewTests(TestCase):
    fixtures = ['nyc_sessions.json', 'nyc_orgs.json', 'nyc_bills.json']
    def test_do_redirect(self):
        bills = NYCBill.objects.all()

        for bill in bills:
            bill_id = bill.identifier

            identifier_title, identifier_number = bill_id.split(' ', 1)
            identifier_title = identifier_title.lower()

            old_slug = '-'.join([identifier_title, identifier_number])

            response = self.client.get(reverse('bill_detail', args=[old_slug]))

            self.assertEqual(response.status_code, 301)

class CommitteeDetailViewTests(TestCase):
    fixtures = ['nyc_orgs.json']

    def test_do_redirect(self):
        organizations = Organization.objects.all()

        for org in organizations:
            old_slug = org.name.lower().replace(' ', '-')

            response = self.client.get(reverse('committee_detail', args=[old_slug]))

            self.assertEqual(response.status_code, 301)

class PersonDetailViewTests(TestCase):
    fixtures = ['nyc_person.json']

    def test_do_redirect(self):
        people = Person.objects.all()

        for person in people:
            old_slug = person.name.lower().replace(' ', '-').replace('.', '')

            response = self.client.get(reverse('person', args=[old_slug]))

            self.assertEqual(response.status_code, 301)

