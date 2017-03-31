import uuid
from django.db import models

# Create your models here.


class User(models.Model):
    # null 是针对数据库而言，如果 null=True, 表示数据库的该字段可以为空。
    # blank 是针对表单的，如果 blank=True，表示你的表单填写该字段的时候可以不填
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


class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    startAt = models.DateTimeField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    taskName = models.CharField(max_length=64, null=True, blank=True)  # 交易类型
    taskContent = models.CharField(max_length=512, null=True, blank=True)  # 交易类型
    taskStatus = models.CharField(max_length=6, null=True, blank=True)  # 交易类型
    senderNumber = models.CharField(max_length=32, null=True, blank=True)  # 支付方式的支付流水
    receiverNumber = models.CharField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.taskName
