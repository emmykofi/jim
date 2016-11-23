from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.flight_list, name='list'),
	url(r'(?P<booking_pk>\d+)/t(?P<step_pk>\d+)/$', views.text_detail, name='text'),
	url(r'(?P<pk>\d+)/$', views.booking_detail, name='detail'),
]