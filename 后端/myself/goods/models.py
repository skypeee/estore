from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model
from users.models import userAddress
import sys
# Create your models here.

User = get_user_model()

class goods_type(models.Model):
    name = models.CharField(max_length=255, default="", verbose_name="商品分类名称")

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
    good_type = models.ForeignKey(goods_type, verbose_name="商品分类")
    good_num = models.IntegerField(default=999, verbose_name="商品数量")

class favorite(models.Model):
    good = models.ForeignKey(goods, verbose_name='商品')
    user = models.ForeignKey(User, verbose_name='用户')
    good_num = models.IntegerField(default=1, verbose_name='商品数量')
    favorite_detail = models.CharField(max_length=255, default='', verbose_name='收藏备注')

class order(models.Model):
    status = (
        (0, "未支付"),
        (1, "已支付")
    )
    good = models.ForeignKey(goods, verbose_name='商品')
    user = models.ForeignKey(User, verbose_name='用户')
    good_num = models.IntegerField(default=1, verbose_name='商品数量')
    order_address = models.CharField(default="", verbose_name="收货地址", max_length=255)
    order_num = models.CharField(default=1 , max_length=10000, verbose_name="订单号")
    order_aceptman = models.CharField(default="", max_length=255, verbose_name="收货人名称")
    order_phone = models.CharField(default="", max_length=255, verbose_name="收货手机号")
    order_time = models.DateTimeField(default=datetime.now, verbose_name="订单时间")
    order_status = models.IntegerField(choices=status, default=0, verbose_name="订单状态")

class shopping(models.Model):
    good = models.ForeignKey(goods, verbose_name='商品')
    user = models.ForeignKey(User, verbose_name='用户')
    shopping_detail = models.CharField(max_length=255, verbose_name='购物车备注')


class Comment(models.Model):
    comment_time = models.DateTimeField(default=datetime.now, max_length=255, verbose_name="评论时间")
    comment_content = models.TextField(verbose_name="评论内容")
    user = models.ForeignKey(User, verbose_name="用户")
    good = models.ForeignKey(goods, verbose_name="订单")
    satisficing = models.CharField(default=0, max_length=255, verbose_name="用户满意度")

class prefer(models.Model):
    user = models.ForeignKey(User, verbose_name="用户")
    good = models.ForeignKey(goods, verbose_name="商品")
    prefer_detail = models.CharField(max_length=255, verbose_name='喜欢备注')

class replay(models.Model):
    user = models.ForeignKey(User,default=1, verbose_name="用户")
    comment = models.ForeignKey(Comment, default=1,verbose_name="评价")
    content = models.CharField(max_length=255, default="", verbose_name="回复")

