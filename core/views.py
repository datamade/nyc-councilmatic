from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Person, Bill, Organization, Action, Event
from haystack.forms import FacetedSearchForm
from datetime import date, timedelta
from itertools import groupby
import councilmatic.city_config as city_config

class CouncilmaticSearchForm(FacetedSearchForm):
    
    def __init__(self, *args, **kwargs):
        self.load_all = True

        super(CouncilmaticSearchForm, self).__init__(*args, **kwargs)

    def no_query_found(self):
        return self.searchqueryset.all()

def city_context(request):
	city_context = {
		'city_name': city_config.CITY_NAME, 
		'city_council_name': city_config.CITY_COUNCIL_NAME, 
		'search_placeholder_text': city_config.SEARCH_PLACEHOLDER_TEXT,
		'search_placeholder_text_short': city_config.SEARCH_PLACEHOLDER_TEXT_SHORT,
		'legislation_type_descriptions': city_config.LEGISLATION_TYPE_DESCRIPTIONS,
	}
	return city_context

@login_required(login_url='/login/')
def index(request):
	one_month_ago = date.today() + timedelta(days=-30)
	recent_legislation = Bill.objects.exclude(last_action_date=None).filter(last_action_date__gt=one_month_ago).order_by('-last_action_date').all()
	recently_passed = [l for l in recent_legislation if l.inferred_status == 'Passed']

	context = {
		'recent_legislation': recent_legislation,
		'recently_passed': recently_passed,
		'next_council_meeting': Event.next_city_council_meeting(),
		'upcoming_committee_meetings': list(Event.upcoming_committee_meetings()),
	}

	return render(request, 'core/index.html', context)

@login_required(login_url='/login/')
def about(request):

	return render(request, 'core/about.html')

def not_found(request):
	return render(request, 'core/404.html')

@login_required(login_url='/login/')
def council_members(request):
	city_council = Organization.objects.filter(ocd_id=city_config.OCD_CITY_COUNCIL_ID).first()
	context = {
		'city_council': city_council
	}

	return render(request, 'core/council_members.html', context)

@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
def committee_detail(request, slug):

	committee = Organization.objects.filter(slug=slug).first()

	if not committee:
		raise Http404("Committee does not exist")

	chairs = committee.memberships.filter(role="CHAIRPERSON")
	memberships = committee.memberships.filter(role="Committee Member")
	committee_description = city_config.COMMITTEE_DESCIPTIONS[committee.slug] if committee.slug in city_config.COMMITTEE_DESCIPTIONS else None

	context = {
		'committee': committee,
		'chairs': chairs,
		'memberships': memberships,
		'committee_description': committee_description,
	}

	return render(request, 'core/committee.html', context)

@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
def events(request, year=None, month=None):

	newest_year = Event.objects.all().order_by('-start_time').first().start_time.year
	oldest_year = Event.objects.all().order_by('start_time').first().start_time.year
	year_range = list(reversed(range(oldest_year, newest_year+1)))
	month_options = [['January', 1],['Febrary',2],['March',3],['April',4],['May',5],['June',6],['July',7],['August',8],['September',9],['October',10],['November',11],['December',12]]

	if not year or not month:
		year = date.today().year
		month = date.today().month

		upcoming_dates = Event.objects.filter(start_time__gt=date.today()).datetimes('start_time', 'day').order_by('start_time')[:50]
		upcoming_events = []
		for d in upcoming_dates:
			if not (upcoming_events and d == upcoming_events[-1][0]):
				events_on_day = Event.objects.filter(start_time__year=d.year).filter(start_time__month=d.month).filter(start_time__day=d.day).order_by('start_time').all()
				upcoming_events.append([d, events_on_day])

		context = {
			'this_month': month,
			'this_year': year,
			'upcoming_events': upcoming_events,
			'year_range': year_range,
			'month_options': month_options,
		}

		return render(request, 'core/events.html', context)
	else:
		year = int(year)
		month = int(month)

		month_dates = Event.objects.filter(start_time__year=year).filter(start_time__month=month).datetimes('start_time', 'day').order_by('start_time')
		month_events = []
		for d in month_dates:
			if not (month_events and d == month_events[-1][0]):
				events_on_day = Event.objects.filter(start_time__year=d.year).filter(start_time__month=d.month).filter(start_time__day=d.day).order_by('start_time').all()
				month_events.append([d, events_on_day])

		context = {
			'this_month': month,
			'this_year': year,
			'first_date': month_dates[0],
			'month_events': month_events,
			'year_range': year_range,
			'month_options': month_options,
		}

		return render(request, 'core/events.html', context)

@login_required(login_url='/login/')
def event_detail(request, slug):

	event = Event.objects.filter(slug=slug).first()
	agenda_items = event.agenda_items.order_by('order').all()
	agenda_deduped = []
	for a in agenda_items:
		if a.description not in agenda_deduped:
			agenda_deduped.append(a.description)

	participants = [ Organization.objects.filter(name=p.entity_name).first() for p in event.participants.all()]
	context = {
		'event': event,
		'participants': participants,
		'agenda_clean': agenda_deduped,
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
