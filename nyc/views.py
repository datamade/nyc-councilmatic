from django.shortcuts import render
from datetime import date, timedelta
from nyc.models import NYCBill
from councilmatic_core.models import Event, Organization
from councilmatic_core.views import *

class NYCIndexView(IndexView):
    template_name = 'nyc/index.html'
    bill_model = NYCBill

class NYCAboutView(AboutView):
    template_name = 'nyc/about.html'

class NYCBillDetailView(BillDetailView):
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

