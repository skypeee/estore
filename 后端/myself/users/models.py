from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
# Create your models here.

class UserProfile(AbstractUser):
    user_phone = models.CharField(max_length=255, default='', verbose_name='用户手机号')
    user_address = models.CharField(default='', max_length=255, verbose_name='用户地址')
    user_signature = models.CharField(default="", max_length=255, verbose_name="用户签名")
    user_img = models.ImageField(default="default.png", max_length=255, verbose_name="用户头像")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.last_name

User = get_user_model()

class userAddress(models.Model):
    default = (
        (0, "默认地址"),
        (1, "非默认")
    )
    user = models.ForeignKey(User, verbose_name="用户")
    content = models.CharField(default="", max_length=255, verbose_name="用户地址")
    isDefault = models.CharField(default=1, choices=default, max_length=255, verbose_name="是否默认")
    name = models.CharField(default="", max_length=255, verbose_name="收货人姓名")
    phone = models.CharField(default="", max_length=255, verbose_name="收货手机号")


    class Meta:
        verbose_name = "地址"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content