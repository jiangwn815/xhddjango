from django.urls import path, re_path, include

from . import views

app_name = 'datamining'
productpatterns = [
    re_path(r'^$', views.product_info_list, name='product_info_list')
]
urlpatterns = [
    # 不区分get post方法都是调用同一个view函数
    path("", views.index, name='index'), # name主要用于模板引用视图函数
    path("bjdata/", views.bjdata, name='bjdata'),
    path("dealxlsx/", views.dealxlsx, name='dealxlsx'),
    path("userlist/", views.userlist, name='userlist'),
    path("collectxls/", views.collectxls, name='collectxls'),
    path("userlist_paginator/", views.userlist_paginator, name='userlist_paginator'),
    path('customer/<int:customer_id>/', views.showcustomer, name='showcustomer'),
    path('user/<int:user_no>/', views.showuser, name='showuser'),
    re_path(r'^name_list/$', views.showname, name='showname'),
    path('product/', include(productpatterns))
]
