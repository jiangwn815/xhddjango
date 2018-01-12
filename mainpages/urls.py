from django.conf.urls import url

from . import views

app_name = 'mainpages'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register, name='register'),
    url(r'^sms$', views.sms, name='sms'),
    url(r'^crawler$', views.crawler, name='crawler'),
    url(r'^crawlerpic$', views.crawlerpic, name='crawlerpic'),
    url(r'^bjdata$', views.bjdata, name='bjdata'),
    url(r'^smslist$', views.smslist, name='smslist'),
    url(r'^smsedit$', views.smsedit, name='smsedit'),
    url(r'^createuser$', views.createuser, name='createuser'),
    url(r'^api/users$', views.users, name='users'),
    url(r'^tasks/index$', views.tasks, name='tasks'),
    url(r'^tasks/create$', views.createtask, name='createtask'),
    url(r'^tasks/view$', views.viewtask, name='viewtask'),
    url(r'^tasks/delete$', views.deletetask, name='deletetask'),
    url(r'^(?P<mobile>[0-9]+)$', views.showuser, name="showuser"),
    url(r'^(?P<mobile>[0-9]+)/info/$', views.info, name="info"),
    url(r'^(?P<mobile>[0-9]+)/useramount/$', views.useramount, name="useramount"),
]