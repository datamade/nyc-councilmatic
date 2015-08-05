from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^committees/$', views.committees, name='committees'),
    url(r'^bill-detail/(.*)/$', views.bill_detail, name='bill_detail')
]