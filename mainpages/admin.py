from django.contrib import admin

# Register your models here.

from .models import User, Order

admin.site.register(User)
admin.site.register(Order)
