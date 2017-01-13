from django.shortcuts import render
from datetime import date, timedelta
from nyc.models import NYCBill
from councilmatic_core.models import Event, Organization, Bill
from councilmatic_core.views import *
from haystack.query import SearchQuerySet

from django.http import HttpResponsePermanentRedirect, HttpResponseNotFound
from django.core.urlresolvers import reverse

class NYCIndexView(IndexView):
    template_name = 'nyc/index.html'
    bill_model = NYCBill

class NYCAboutView(AboutView):
    template_name = 'nyc/about.html'

class NYCBillDetailView(BillDetailView):
    model = NYCBill

    def dispatch(self, request, *args, **kwargs):
        slug = self.kwargs['slug']

        try:
            bill = self.model.objects.get(slug=slug)
            response = super().dispatch(request, *args, **kwargs)
        except NYCBill.DoesNotExist:
            bill = None

        if bill is None:
            identifier_title, identifier_number = slug.split('-', 1)
            if identifier_title == 'lu':
                identifier_title = 'LU'
            else:
                identifier_title = identifier_title.title()

            full_identifier = ' '.join([identifier_title, identifier_number])
            try:
                bill = self.model.objects.get(identifier=full_identifier)
                response = HttpResponsePermanentRedirect(reverse('bill_detail', args=[bill.slug]))
            except NYCBill.DoesNotExist:
                response = HttpResponseNotFound()

        return response


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

class NYCCouncilmaticFacetedSearchView(CouncilmaticFacetedSearchView):

    def build_form(self, form_kwargs=None):
        form = super(CouncilmaticFacetedSearchView, self).build_form(form_kwargs=form_kwargs)

        # For faceted search functionality.
        if form_kwargs is None:
            form_kwargs = {}

        form_kwargs['selected_facets'] = self.request.GET.getlist("selected_facets")

        # For remaining search functionality.
        data = None
        kwargs = {
            'load_all': self.load_all,
        }

        sqs = SearchQuerySet().facet('bill_type')\
                      .facet('sponsorships', sort='index')\
                      .facet('controlling_body')\
                      .facet('inferred_status')\
                      .highlight()

        if form_kwargs:
            kwargs.update(form_kwargs)

        if len(self.request.GET):
            data = self.request.GET
            dataDict = dict(data)

        if self.searchqueryset is not None:
            kwargs['searchqueryset'] = sqs

            try:
                for el in dataDict['sort_by']:
                    # Do this, because sometimes the 'el' may include a '?' from the URL
                    if 'date' in el:
                        try:
                            dataDict['ascending']
                            kwargs['searchqueryset'] = sqs.order_by('last_action_date')
                        except:
                            kwargs['searchqueryset'] = sqs.order_by('-last_action_date')
                    if 'title' in el:
                        try:
                            dataDict['descending']
                            kwargs['searchqueryset'] = sqs.order_by('-sort_name')
                        except:
                            kwargs['searchqueryset'] = sqs.order_by('sort_name')
                    if 'relevance' in el:
                        kwargs['searchqueryset'] = sqs

            except:
                kwargs['searchqueryset'] = sqs.order_by('-last_action_date')

        return self.form_class(data, **kwargs)
