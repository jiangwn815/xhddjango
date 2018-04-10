from django.urls import path

from . import views

app_name = 'datamining'
urlpatterns = [
    path("", views.index, name='index'), # name主要用于模板引用视图函数
    path("bjdata/", views.bjdata, name='bjdata'),
    path("dealxlsx/", views.dealxlsx, name='dealxlsx'),
    path("userlist/", views.userlist, name='userlist'),
    path("collectxls/", views.collectxls, name='collectxls'),
    path("userlist_paginator/", views.userlist_paginator, name='userlist_paginator'),
    path('customer/<int:customer_id>/', views.showcustomer, name='showcustomer'),
    path('user/<int:user_no>/', views.showuser, name='showuser')
]
