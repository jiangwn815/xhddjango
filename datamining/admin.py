from django.contrib import admin

# Register your models here.
from .models import Userinfo


class UserinfoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user_no']}),
        ('关键信息', {'fields': ['mobile_no', 'in_time', 'user_state']}),
        ('发展信息', {'fields': ['seller_channel_third', 'seller_channel_fifth', 'seller_channel_sixth', 'seller_name',
                             'brokerage_channel', 'double_seller']}),
        ('资费信息', {'fields': ['mainproduct_second', 'singleproduct_sub', 'subscribe_plan', 'charge_plan']}),
    ]


admin.site.register(Userinfo, UserinfoAdmin)
