from django.shortcuts import render
from .models import Person, Bill, Organization, Action

def index(request):
	recent_legislation = Bill.objects.order_by('date_updated')[:10]
	context = {
		'recent_legislation': recent_legislation
	}

	return render(request, 'nyc/index.html', context)

def about(request):
	return render(request, 'nyc/about.html')

def search(request):
	return render(request, 'nyc/search.html')

def council_members(request):
	city_council = Organization.objects.filter(ocd_id='ocd-organization/389257d3-aefe-42df-b3a2-a0d56d0ea731').first()
	context = {
		'city_council': city_council
	}

	return render(request, 'nyc/council_members.html', context)

def bill_detail(request, bill_id):

	legislation = Bill.objects.filter(ocd_id=bill_id).first()

	context={
		'legislation': legislation
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

def committee_detail(request, org_id):

	committee = Organization.objects.filter(ocd_id=org_id).first()

	chairs = committee.memberships.filter(role="CHAIRPERSON")
	memberships = committee.memberships.filter(role="Committee Member")

	context = {
		'committee': committee,
		'chairs': chairs,
		'memberships': memberships
	}

	return render(request, 'nyc/committee.html', context)

def person(request, person_id):

	person = Person.objects.filter(ocd_id=person_id).first()

	chairs = person.memberships.filter(role="CHAIRPERSON")
	memberships = person.memberships.filter(role="Committee Member")

	context = {
		'person': person,
		'chairs': chairs,
		'memberships': memberships,
	}

	return render(request, 'nyc/person.html', context)
