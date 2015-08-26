from django.shortcuts import render
from django.http import Http404
from .models import Person, Bill, Organization, Action
from haystack.forms import FacetedSearchForm

class CouncilmaticSearchForm(FacetedSearchForm):
    
    def __init__(self, *args, **kwargs):
        self.load_all = True

        super(CouncilmaticSearchForm, self).__init__(*args, **kwargs)

    def no_query_found(self):
        return self.searchqueryset.all()

def index(request):
	recent_legislation = Bill.objects.exclude(bill_type='NO TYPE').exclude(last_action_date=None).order_by('-last_action_date')[:10]
	context = {
		'recent_legislation': recent_legislation
	}

	return render(request, 'nyc/index.html', context)

def about(request):
	return render(request, 'nyc/about.html')

def not_found(request):
	return render(request, 'nyc/404.html')

def search(request):
	return render(request, 'nyc/search.html')

def council_members(request):
	city_council = Organization.objects.filter(ocd_id='ocd-organization/389257d3-aefe-42df-b3a2-a0d56d0ea731').first()
	context = {
		'city_council': city_council
	}

	return render(request, 'nyc/council_members.html', context)

def bill_detail(request, slug):

	legislation = Bill.objects.filter(slug=slug).first()
	
	if not legislation:
		raise Http404("Legislation does not exist")

	actions = legislation.actions.all().order_by('-order')

	context={
		'legislation': legislation,
		'actions': actions
	}

	return render(request, 'nyc/legislation.html', context)

def committees(request):

	committees = Organization.committees().filter(name__startswith='Committee')

	subcommittees = Organization.committees().filter(name__startswith='Subcommittee')

	taskforces = Organization.committees().filter(name__startswith='Task Force')

	context={
		'committees': committees,
		'subcommittees': subcommittees,
		'taskforces': taskforces,
	}

	return render(request, 'nyc/committees.html', context)

def committee_detail(request, slug):

	committee = Organization.objects.filter(slug=slug).first()

	if not committee:
		raise Http404("Committee does not exist")

	chairs = committee.memberships.filter(role="CHAIRPERSON")
	memberships = committee.memberships.filter(role="Committee Member")

	context = {
		'committee': committee,
		'chairs': chairs,
		'memberships': memberships
	}

	return render(request, 'nyc/committee.html', context)

def person(request, slug):

	person = Person.objects.filter(slug=slug).first()

	if not person:
		raise Http404("Person does not exist")

	sponsorships = person.sponsorships.order_by('-bill__last_action_date')[:20]

	chairs = person.memberships.filter(role="CHAIRPERSON")
	memberships = person.memberships.filter(role="Committee Member")

	context = {
		'person': person,
		'chairs': chairs,
		'memberships': memberships,
		'sponsorships': sponsorships,
		'sponsored_legislation': [s.bill for s in sponsorships]
	}

	return render(request, 'nyc/person.html', context)
