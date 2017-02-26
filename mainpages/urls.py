from django.conf.urls import url

from . import views

app_name = 'mainpages'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<mobile>[0-9]+)$', views.showuser, name="showuser"),
    url(r'^(?P<user_id>[0-9]+)/info/$', views.info, name="info"),
    url(r'^(?P<user_id>[0-9]+)/user_amount/$', views.user_amount, name="user_amount"),
]