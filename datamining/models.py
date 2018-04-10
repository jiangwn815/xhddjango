import uuid
import django.utils.timezone as timezone
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

    class Meta:
        ordering = ['mobile_no']

    def __str__(self):
        return self.user_no or self.mobile_no

    @property
    def section_no(self):
        return self.mobile_no[0:3]

    @property
    def in_time_year(self):
        return self.in_time[0:4]


class Baseuser(models.Model):
    ID_TYPES = (
        ('I', 'ID Card'),
        ('P', 'Passport'),
        ('M', 'Military ID'),
        ('B', 'Business Licence'),
        ('O', 'Others')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=32)
    id_type = models.CharField(max_length=1, choices=ID_TYPES)
    id_no = models.CharField(max_length=18)
    date_created = models.DateTimeField(default=timezone.now)
    date_update = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        abstract = True


class TeleUser(Baseuser):
    customer_id = models.CharField(max_length=20)
    user_no = models.CharField(max_length=20)
    mobile_no = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        ordering = ['-customer_id']


class Bill(models.Model):
    customer_id = models.CharField(max_length=20)
    user_no = models.CharField(max_length=20, blank=True, null=True)
    account_date = models.DateField()
    zz_income = models.DecimalField(max_digits=22, decimal_places=2, blank=True, null=True)
    zd_income = models.DecimalField(max_digits=22, decimal_places=2, blank=True, null=True)

    class Meta:
        get_latest_by = ['customer_id', 'user_no', '-account_date']  # 客户编号、用户编号升序，账期降序


class ResourceUsage(models.Model):
    customer_id = models.CharField(max_length=20)
    user_no = models.CharField(max_length=20, blank=True, null=True)
    account_date = models.DateField()
    text_usage = models.IntegerField(blank=True, null=True)
    call_times = models.IntegerField(blank=True, null=True)
    call_duration = models.IntegerField(blank=True, null=True)
    data_usage = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True   # 如果为False则django不会主动创建或删除table，应用于使用已有table的情景
