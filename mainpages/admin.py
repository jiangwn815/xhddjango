from django.contrib import admin

# Register your models here.

from .models import User, Order, Task

admin.site.register(User)
admin.site.register(Order)
admin.site.register(Task)
