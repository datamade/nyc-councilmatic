from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from councilmatic_core.models import Organization
from nyc.models import NYCBill

class BillDetailViewTests(TestCase):
    fixtures = ['sessions.json', 'orgs.json', 'bills.json']
    def test_do_redirect(self):
        bills = NYCBill.objects.all()

        for bill in bills:
            bill_id = bill.identifier

            identifier_title, identifier_number = bill_id.split(' ', 1)
            identifier_title = identifier_title.lower()

            old_slug = '-'.join([identifier_title, identifier_number])
            print(old_slug)
            response = self.client.get(reverse('bill_detail', args=[old_slug]))

            self.assertEqual(response.status_code, 301)
        # self.assertTrue(True)
        # response = self.client.get(reverse('bill_detail', args=[old_slug]))
        # response = self.client.get(reverse('bill_detail', args=['t-2017-5413-85adb6086065']))
        # response = self.client.get('/legislation/t-2017-5413-85adb6086065/')
        # response = self.client.get('/')
        # response = self.client.get(reverse('bill_detail', args=['t-2017-5413']))
        # self.assertEqual(response.status_code, 301)

class CommitteeDetailViewTests(TestCase):
    fixtures = ['orgs.json']

    def test_do_redirect(self):
        organizations = Organization.objects.all()

        for org in organizations:
            old_slug = org.name.lower().replace(' ', '-')
            print(old_slug)
            response = self.client.get(reverse('committee_detail', args=[old_slug]))

            self.assertEqual(response.status_code, 301)