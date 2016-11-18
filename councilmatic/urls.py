from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from haystack.query import SearchQuerySet, EmptySearchQuerySet
from councilmatic_core.views import CouncilmaticSearchForm, CouncilmaticFacetedSearchView
from councilmatic_core.feeds import CouncilmaticFacetedSearchFeed
from nyc.views import *
from nyc.feeds import *
from django.views.decorators.cache import never_cache

from councilmatic.settings import *

# sqs = SearchQuerySet().facet('bill_type')\
#                       .facet('sponsorships', sort='index')\
#                       .facet('controlling_body')\
#                       .facet('inferred_status')\
#                       .highlight()

patterns = ([
    url(r'^committees/$', NYCCommitteesView.as_view(), name='committees'),
    url(r'^search/rss/',
        NYCCouncilmaticFacetedSearchFeed(), name='councilmatic_search_feed'),
    url(r'^search/', CouncilmaticFacetedSearchView(searchqueryset=EmptySearchQuerySet,
                                                   form_class=CouncilmaticSearchForm),
                     name='search'),
    url(r'^$', NYCIndexView.as_view(), name='index'),
    url(r'^about/$', NYCAboutView.as_view(), name='about'),
    url(r'^legislation/(?P<slug>[^/]+)/$', NYCBillDetailView.as_view(), name='bill_detail'),
    url(r'^legislation/(?P<slug>[^/]+)/widget/$', NYCBillWidgetView.as_view(), name='bill_widget'),
    url(r'^legislation/(?P<slug>[^/]+)/rss/$', NYCBillDetailActionFeed(), name='bill_detail_action_feed'),
], settings.APP_NAME)

urlpatterns = [
    url(r'', include(patterns)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('councilmatic_core.urls')),
]

if (USING_NOTIFICATIONS):
    urlpatterns.extend([
        url(r'', include('notifications.urls')),
    ])
