from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='abouts'),
    url(r'^committees/$', views.committees, name='committees'),
    url(r'^council-members/$', views.council_members, name='council_members'),
    url(r'^committee/(.*)/$', views.committee_detail, name='committee_detail'),
    url(r'^legislation/(.*)/$', views.bill_detail, name='bill_detail'),
    url(r'^person/(.*)/$', views.person, name='person'),
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^logout/$', views.user_logout, name='user_logout'),
    url(r'^events/$', views.events, name='events'),
    url(r'^events/(.*)/(.*)/$', views.events, name='events'),
]