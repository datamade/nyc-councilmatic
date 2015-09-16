from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Person, Bill, Organization, Action, Event
from haystack.forms import FacetedSearchForm
from datetime import date, timedelta
from itertools import groupby
from councilmatic.city_config import LEGISLATION_TYPE_DESCRIPTIONS, COMMITTEE_DESCIPTIONS

class CouncilmaticSearchForm(FacetedSearchForm):
    
    def __init__(self, *args, **kwargs):
        self.load_all = True

        super(CouncilmaticSearchForm, self).__init__(*args, **kwargs)

    def no_query_found(self):
        return self.searchqueryset.all()

@login_required(login_url='/login/')
def index(request):
	#recent_legislation = Bill.objects.exclude(last_action_date=None).order_by('-last_action_date')[:10]
	one_month_ago = date.today() + timedelta(days=-30)
	recent_legislation = Bill.objects.exclude(last_action_date=None).filter(last_action_date__gt=one_month_ago).order_by('-last_action_date').all()
	recently_passed = [l for l in recent_legislation if l.inferred_status == 'Passed']

	context = {
		'recent_legislation': recent_legislation,
		'recently_passed': recently_passed,
	}

	return render(request, 'core/index.html', context)

def about(request):
	context = {
		'legislation_type_descriptions': LEGISLATION_TYPE_DESCRIPTIONS,
	}
	return render(request, 'core/about.html', context)

def not_found(request):
	return render(request, 'core/404.html')

def search(request):
	return render(request, 'core/search.html')

def council_members(request):
	city_council = Organization.objects.filter(ocd_id='ocd-organization/389257d3-aefe-42df-b3a2-a0d56d0ea731').first()
	context = {
		'city_council': city_council
	}

	return render(request, 'core/council_members.html', context)

def bill_detail(request, slug):

	legislation = Bill.objects.filter(slug=slug).first()
	
	if not legislation:
		raise Http404("Legislation does not exist")

	actions = legislation.actions.all().order_by('-order')

	context={
		'legislation': legislation,
		'actions': actions
	}

	return render(request, 'core/legislation.html', context)

def committees(request):

	committees = Organization.committees().filter(name__startswith='Committee')

	subcommittees = Organization.committees().filter(name__startswith='Subcommittee')

	taskforces = Organization.committees().filter(name__startswith='Task Force')

	context={
		'committees': committees,
		'subcommittees': subcommittees,
		'taskforces': taskforces,
	}

	return render(request, 'core/committees.html', context)

def committee_detail(request, slug):

	committee = Organization.objects.filter(slug=slug).first()

	if not committee:
		raise Http404("Committee does not exist")

	chairs = committee.memberships.filter(role="CHAIRPERSON")
	memberships = committee.memberships.filter(role="Committee Member")
	committee_description = COMMITTEE_DESCIPTIONS[committee.slug] if committee.slug in COMMITTEE_DESCIPTIONS else None

	context = {
		'committee': committee,
		'chairs': chairs,
		'memberships': memberships,
		'committee_description': committee_description,
	}

	return render(request, 'core/committee.html', context)

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

	return render(request, 'core/person.html', context)


def events(request, year=None, month=None):

	if not year or not month:
		year = date.today().year
		month = date.today().month

		upcoming_dates = Event.objects.filter(start_time__gt=date.today()).datetimes('start_time', 'day').order_by('start_time')[:50]
		upcoming_events = []
		for d in upcoming_dates:
			events_on_day = Event.objects.filter(start_time__year=d.year).filter(start_time__month=d.month).filter(start_time__day=d.day).order_by('start_time').all()
			upcoming_events.append([d, events_on_day])

		past_dates = Event.objects.datetimes('start_time', 'day').order_by('-start_time')[:50]
		past_events = []
		for d in past_dates:
			events_on_day = Event.objects.filter(start_time__year=d.year).filter(start_time__month=d.month).filter(start_time__day=d.day).order_by('start_time').all()
			past_events.append([d, events_on_day])

		context = {
			'upcoming_events': upcoming_events,
			'past_events': past_events,
		}

		return render(request, 'core/events.html', context)
	else:
		year = int(year)
		month = int(month)

		month_dates = Event.objects.filter(start_time__year=year).filter(start_time__month=month).datetimes('start_time', 'day').order_by('start_time')
		month_events = []
		for d in month_dates:
			events_on_day = Event.objects.filter(start_time__year=d.year).filter(start_time__month=d.month).filter(start_time__day=d.day).order_by('start_time').all()
			month_events.append([d, events_on_day])

		context = {
			'first_date': month_dates[0],
			'month_events': month_events,
		}

		return render(request, 'core/events.html', context)

def event_detail(request, slug):

	event = Event.objects.filter(slug=slug).first()
	context = {
		'event': event
	}

	return render(request, 'core/event.html', context)

def user_login(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			if user is not None:
				login(request, user)
				return redirect('index')
	else:
		form = AuthenticationForm()

	return render(request, 'core_user/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('index')
