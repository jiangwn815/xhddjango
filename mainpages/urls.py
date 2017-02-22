from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<user_id>[0-9]+)$', views.show_user, name="show_user"),
    url(r'^(?P<user_id>[0-9]+)/info/$', views.info, name="info"),
    url(r'^(?P<user_id>[0-9]+)/user_amount/$', views.user_amount, name="user_amount"),
]