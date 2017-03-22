from django.conf.urls import url

from . import views

app_name = 'mainpages'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register, name='register'),
    url(r'^sms$', views.sms, name='sms'),
    url(r'^(?P<mobile>[0-9]+)$', views.showuser, name="showuser"),
    url(r'^(?P<mobile>[0-9]+)/info/$', views.info, name="info"),
    url(r'^(?P<mobile>[0-9]+)/useramount/$', views.useramount, name="useramount"),
]