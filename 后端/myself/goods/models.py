from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class goods(models.Model):
    color_status = (
        (1, "黑"),
        (2, "白"),
        (3, '灰')
    )
    good_name = models.CharField(max_length=255, default='', verbose_name='商品名称')
    good_price = models.IntegerField(verbose_name='商品价格', default=0)
    good_brand = models.CharField(max_length=255, default='', verbose_name='商品品牌')
    good_color = models.CharField(choices=color_status, default=1, verbose_name="颜色", max_length=255)
    good_img = models.ImageField(default='', upload_to="goods/%Y/%m", verbose_name='用户头像', max_length=100)
    good_content = models.CharField(max_length=255, default='', verbose_name='商品内容')
    good_parameter = models.CharField(max_length=255, default='', verbose_name='商品参数')
    good_type = models.CharField(max_length=255, default='', verbose_name='商品类型')
    good_num = models.IntegerField(default=999, verbose_name="商品数量")

class limitGood(models.Model):
    good = models.ForeignKey(goods, verbose_name='商品')
    last_time = models.DateTimeField(max_length=255, default=datetime.now, verbose_name='截止时间')

class favorite(models.Model):
    good = models.ForeignKey(goods, verbose_name='商品')
    user = models.ForeignKey(User, verbose_name='用户')
    good_num = models.IntegerField(default=1, verbose_name='商品数量')
    favorite_detail = models.CharField(max_length=255, default='', verbose_name='收藏备注')

class order(models.Model):
    good = models.ForeignKey(goods, verbose_name='商品')
    user = models.ForeignKey(User, verbose_name='用户')
    order_address = models.CharField(max_length=255, verbose_name='收货地址')
    good_num = models.IntegerField(default=1, verbose_name='商品数量')

class shopping(models.Model):
    good = models.ForeignKey(goods, verbose_name='商品')
    user = models.ForeignKey(User, verbose_name='用户')
    shopping_detail = models.CharField(max_length=255, verbose_name='购物车备注')



