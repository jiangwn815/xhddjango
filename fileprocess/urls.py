from django.urls import path, re_path, include

from . import views

app_name = 'fileprocess'

urlpatterns = [
    # 不区分get post方法都是调用同一个view函数
    path("", views.index, name='index'), # name主要用于模板引用视图函数

]
