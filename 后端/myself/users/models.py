from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserProfile(AbstractUser):
    user_phone = models.CharField(max_length=255, default='', verbose_name='用户手机号')
    user_img = models.ImageField(default='', upload_to='user/%Y/%M', verbose_name='用户头像')
    user_address = models.CharField(default='', max_length=255, verbose_name='用户地址')


    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.last_name
