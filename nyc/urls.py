from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='abouts'),
    url(r'^search/$', views.search, name='search'),
    url(r'^committees/$', views.committees, name='committees'),
    url(r'^council-members/$', views.council_members, name='council_members'),
    url(r'^committee-detail/(.*)/$', views.committee_detail, name='committee_detail'),
    url(r'^bill-detail/(.*)/$', views.bill_detail, name='bill_detail'),
    url(r'^person/(.*)/$', views.person, name='person'),
]