from django.db import models

# Create your models here.
class Userinfo(models.Model):
    user_no = models.CharField(max_length=12, primary_key=True)
    mobile_no = models.CharField(max_length=12)
    in_time = models.CharField(max_length=8, blank=True, null=True)
    out_time = models.CharField(max_length=8, blank=True, null=True)
    out_type = models.CharField(max_length=12, blank=True, null=True)
    user_state = models.CharField(max_length=10, blank=True, null=True)
    user_state_starttime = models.CharField(max_length=8, blank=True, null=True)
    user_online_time = models.CharField(max_length=4, blank=True, null=True)
    double_seller = models.CharField(max_length=128, blank=True, null=True)
    brokerage_channel = models.CharField(max_length=128, blank=True, null=True)
    seller_name = models.CharField(max_length=128, blank=True, null=True)
    seller_channel_third = models.CharField(max_length=128, blank=True, null=True)
    seller_channel_fifth = models.CharField(max_length=128, blank=True, null=True)
    seller_channel_sixth = models.CharField(max_length=128, blank=True, null=True)
    subscribe_plan = models.CharField(max_length=128, blank=True, null=True)
    charge_plan = models.CharField(max_length=128, blank=True, null=True)
    mainproduct_second = models.CharField(max_length=64, blank=True, null=True)
    singleproduct_sub = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):

        return self.user_no or self.mobile_no

