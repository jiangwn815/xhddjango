import uuid
from django.db import models

# Create your models here.


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    version = models.BigIntegerField()
    nickname = models.CharField(max_length=128)
    sex = models.IntegerField(default=0)
    wxlanguage = models.CharField(max_length=8)
    city = models.CharField(max_length=64)
    province = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    openid = models.CharField(max_length=128)
    unionid = models.CharField(max_length=128)
    groupid = models.IntegerField()
    subscribe_time = models.DateTimeField()
    subscribe = models.IntegerField()
    headimgurl = models.URLField()
    remark = models.CharField(max_length=128)
    email = models.CharField(max_length=32)
    mobile = models.CharField(max_length=128)
    passwd = models.CharField(max_length=128)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    settlement_total_fee = models.IntegerField()  # 应结订单金额
    total_fee = models.IntegerField()  #  订单金额
    trade_type = models.CharField(max_length=8)  # 交易类型
    transaction_id = models.CharField(max_length=32)  # 支付方式的支付流水
    payment_type = models.CharField(max_length=6)
    out_trade_no = models.CharField(max_length=32)  # 订单号
    time_end = models.CharField(max_length=32)  # 支付完成时间
