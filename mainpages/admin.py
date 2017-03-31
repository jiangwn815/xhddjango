from django.contrib import admin

# Register your models here.

from .models import User, Order, YdysTask

admin.site.register(User)
admin.site.register(Order)
admin.site.register(YdysTask)
