from django.contrib import admin
# Register your models here.
from .models import Productinfo, TeleUser, Bill, ResourceUsage, TeleDepartment


class UserinfoAdmin(admin.ModelAdmin):
    list_display = ('user_no', 'mobile_no', 'seller_channel_third', 'charge_plan')
    list_filter = ['charge_plan']
    search_fields = ['mobile_no']
    fieldsets = [
        (None, {'fields': ['user_no']}),
        ('关键信息', {'fields': ['mobile_no', 'in_time', 'user_state']}),
        ('发展信息', {'fields': ['seller_channel_third', 'seller_channel_fifth', 'seller_channel_sixth', 'seller_name',
                             'brokerage_channel', 'double_seller']}),
        ('资费信息', {'fields': ['mainproduct_second', 'singleproduct_sub', 'subscribe_plan', 'charge_plan']}),
    ]


admin.site.register(Productinfo, UserinfoAdmin)
admin.site.register(TeleUser)
admin.site.register(Bill)
admin.site.register(ResourceUsage)
admin.site.register(TeleDepartment)
