from django.urls import path

from . import views

app_name = 'dataming'
urlpatterns = [
    path("", views.index, name='index'), # name主要用于模板引用视图函数
    path("bjdata", views.bjdata, name='bjdata'),
    path("dealxlsx", views.dealxlsx, name='dealxlsx')

]