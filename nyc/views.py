from django.shortcuts import render
from datetime import date, timedelta
from nyc.models import NYCBill
from councilmatic_core.models import Event, Organization, Person
from councilmatic_core.views import *
import googleanalytics as ga


class NYCIndexView(IndexView):
    template_name = 'nyc/index.html'
    bill_model = NYCBill

    def extra_context(self):
        extra_context = {}

        extra_context['analytics'] = self.get_analytics_data()

        return extra_context

    def get_analytics_data(self):

        profile = ga.authenticate(identity='nyc-councilmatic',
                interactive=True,
                save=True,
                account='Councilmatic',
                webproperty='NYC Councilmatic',
                profile='NYC Councilmatic')

        month_views = profile.core.query.metrics('pageviews')\
                            .dimensions('pagepath')\
                            .monthly(months=-1)\
                            .sort('pageviews', descending=True)

        top_bills = []
        top_people = []
        for date, page, count in month_views.rows:
            if len(top_people)<5 and page.startswith('/person/'):
                slug = page.split('/')[2]
                top_people.append(Person.objects.get(slug=slug))
            if len(top_bills)<5 and page.startswith('/legislation/'):
                slug = page.split('/')[2]
                top_bills.append(self.bill_model.objects.get(slug=slug))

        analytics_blob = {
            'top_bills': top_bills,
            'top_people': top_people,
        }

        return analytics_blob


class NYCAboutView(AboutView):
    template_name = 'nyc/about.html'

class NYCBillDetailView(BillDetailView):
    model = NYCBill

class NYCBillWidgetView(BillWidgetView):
    model = NYCBill

class NYCCommitteesView(CommitteesView):

    def get_queryset(self):
        return []
    
    def get_context_data(self, **kwargs):
        context = super(CommitteesView, self).get_context_data(**kwargs)

        committees = Organization.committees().filter(name__startswith='Committee')
        context['committees'] = [c for c in committees if c.memberships.all()]
        
        subcommittees = Organization.committees().filter(name__startswith='Subcommittee')
        context['subcommittees'] = [c for c in subcommittees if c.memberships.all()]

        taskforces = Organization.committees().filter(name__startswith='Task Force')
        context['taskforces'] = [c for c in taskforces if c.memberships.all()]
        
        return context

