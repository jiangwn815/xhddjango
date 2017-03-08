import uuid
from django.db import models

# Create your models here.


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    version = models.BigIntegerField(null=True, blank=True)
    nickname = models.CharField(max_length=128, null=True, blank=True)
    sex = models.IntegerField(default=0, null=True, blank=True)
    wxlanguage = models.CharField(max_length=8, null=True, blank=True)
    city = models.CharField(max_length=64, null=True, blank=True)
    province = models.CharField(max_length=64, null=True, blank=True)
    country = models.CharField(max_length=64, null=True, blank=True)
    openid = models.CharField(max_length=128, null=True, blank=True)
    unionid = models.CharField(max_length=128, null=True, blank=True)
    groupid = models.IntegerField(null=True, blank=True)
    subscribe_time = models.DateTimeField(null=True, blank=True)
    subscribe = models.IntegerField(default=0, null=True, blank=True)
    headimgurl = models.URLField(null=True, blank=True)
    remark = models.CharField(max_length=128, null=True, blank=True)
    email = models.CharField(max_length=32, null=True, blank=True)
    mobile = models.CharField(max_length=128)
    passwd = models.CharField(max_length=128)

    def __str__(self):
        return self.mobile


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    settlement_total_fee = models.DecimalField(max_digits=25, decimal_places=2)  # 应结订单金额
    total_fee = models.DecimalField(max_digits=25, decimal_places=2)  #  订单金额
    trade_type = models.CharField(max_length=8, null=True, blank=True)  # 交易类型
    transaction_id = models.CharField(max_length=32, null=True, blank=True)  # 支付方式的支付流水
    payment_type = models.CharField(max_length=6, null=True, blank=True)
    out_trade_no = models.CharField(max_length=32)  # 订单号
    time_end = models.CharField(max_length=32, null=True, blank=True)  # 支付完成时间

    def __str__(self):
        return self.out_trade_no
