import uuid
import django.utils.timezone as timezone
from django.db import models


# Create your models here.
class Productinfo(models.Model):
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
    type = models.CharField(max_length=32, blank=True, null=True)
    wechat_id = models.CharField(max_length=32, blank=True, null=True)
    wechat_bind_time = models.DateTimeField(blank=True, null=True)
    open_id = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        ordering = ['-customer_id']
        indexes = [
            models.Index(fields=['user_no']),
            models.Index(fields=['customer_id'], name='customer_id_idx'),
        ]
        permissions = (
            ('access_teledata', 'Can access tele related data'),
        )


class KDUser(models.Model):
    user_no = models.CharField(primary_key=True, max_length=20)
    mobile_no = models.CharField(max_length=12, blank=True, null=True)
    type = models.CharField(max_length=32, blank=True, null=True)
    wechat_id = models.CharField(max_length=32, blank=True, null=True)
    wechat_bind_time = models.DateTimeField(blank=True, null=True)
    open_id = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['user_no', 'mobile_no']),
            models.Index(fields=['mobile_no'], name='mobile_no_idx'),
        ]

    def __str__(self):
        return "用户编号："+self.user_no+"|服务号码"+self.mobile_no


class WechatUser(models.Model):
    user_no = models.CharField(max_length=20)
    mobile_no = models.CharField(max_length=12, blank=True, null=True)
    type = models.CharField(max_length=32, blank=True, null=True)
    wechat_id = models.CharField(max_length=32, blank=True, null=True)
    wechat_bind_time = models.DateTimeField(blank=True, null=True)
    open_id = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['user_no']),
            models.Index(fields=['open_id'], name='open_id_idx'),
        ]

    def __str__(self):
        return "用户编号："+self.user_no+"|服务号码"+self.mobile_no


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


class TeleDepartment(models.Model):
    name = models.CharField(max_length=64)
    department_id = models.CharField(max_length=32, blank=True, null=True)
    level = models.IntegerField()
    superior = models.ForeignKey('TeleDepartment', on_delete= models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class SubscribePlan(models.Model):
    name = models.CharField(max_length=64)
    plan_id_local = models.CharField(max_length=32, blank=True, null=True)
    plan_id_global = models.CharField(max_length=32, blank=True, null=True)
    minimum_charge = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_update = models.DateTimeField('修改时间', auto_now=True)


class CommissionRecord(models.Model):
    user = models.ForeignKey(TeleUser, on_delete=models.CASCADE, blank=True, null=True)
    user_state = models.CharField(max_length=12, blank=True, null=True)
    comission_in_time = models.DateTimeField(blank=True, null=True)
    commission_strategy = models.CharField(max_length=64, blank=True, null=True)
    comission_value = models.DecimalField(max_digits=16, decimal_places=2)
    agency_name = models.CharField(max_length=64)
    agency_id = models.CharField(max_length=12)
    agency_code = models.CharField(max_length=12)
    bundling_phone = models.CharField(max_length=64, blank=True, null=True)
    comission_channel = models.CharField(max_length=24, blank=True, null=True)
    agency_channel = models.CharField(max_length=24, blank=True, null=True)
    account_date = models.CharField(max_length=6)


class MobileOfAgent(models.Model):
    mobile = models.CharField(max_length=11, primary_key=True)
    channel_name =  models.CharField(max_length=32)
    phone_num_status =  models.CharField(max_length=12)
    add_time = models.DateTimeField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['mobile'])

        ]
        ordering = ['add_time']