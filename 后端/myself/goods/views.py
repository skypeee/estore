from django.shortcuts import render
from .serializers import goodCreateSerializer, goodSerializer, GoodUpdateSerializer, FavoriteSerializer, orderCreateSerializer\
    , FavoriteUpdateSerializer, FavoriteCreateSerializer, orderSerializer, CommentSerializer, CommentCreateSerializer,\
    ReplaySerializer, ReplayCreateSerializer, GoodTypeSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import status, generics, views, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .filter import GoodFilter, CommentFilter, OrderFilter, ReplayFilter, FavoriteFilter, GoodTypeFilter
from .models import goods, favorite, order, Comment, replay, goods_type
from users.models import userAddress
from .schemas import OrderSchema
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from alipay import AliPay
from django.contrib.auth import get_user_model
from datetime import datetime
import re
# Create your views here.
User = get_user_model()

class SelfPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100

class GoodListView(generics.ListAPIView):
    queryset = goods.objects.all()
    serializer_class = goodSerializer
    pagination_class = SelfPagination
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    search_fields = ('=good_type', 'good_brand', 'good_name', 'good_content')
    filter_class = GoodFilter

class GoodCreateView(generics.CreateAPIView):
    serializer_class = goodCreateSerializer

    def post(self, request, *args, **kwargs):
        GoodSerializer = goodCreateSerializer(data=request.data)
        print(GoodSerializer)
        if GoodSerializer.is_valid():
            GoodSerializer.save()
        else:
            return Response(data={'code': 400, 'detail': '参数错误'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data={'code': 201, 'detail': '创建成功'}, status=status.HTTP_201_CREATED)

class GoodDeleteView(views.APIView):
    def post(self, request):
        good_id = request.data.get('good_id')
        if good_id is None:
            return Response(data={'code': 400, 'detail': '参数错误'}, status=status.HTTP_400_BAD_REQUEST)
        good = goods.objects.filter(id=good_id)
        if good.exists():
            good.delete()
            return Response(data={'code': 200, 'detail': '删除成功'}, status=status.HTTP_200_OK)
        else:
            return Response(data={'code': 400, 'detail': '商品不存在'}, status=status.HTTP_400_BAD_REQUEST)

class GoodUpdateView(generics.GenericAPIView):
    queryset = goods.objects.all()
    serializer_class = GoodUpdateSerializer

    def post(self, request):
        try:
            instance = goods.objects.filter(id=request.data.get('id'))[0]
        except:
            return Response(data={'code': 400, 'detail': '商品id不存在'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            serializer = GoodUpdateSerializer()
            serializer.update(instance=instance, validated_data=request.data)
        except:
            return Response(data={'code': 400, 'detail': '商品id不存在'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data={'code': 200, 'detail': '更新成功'}, status=status.HTTP_200_OK)

class FavoriteListView(generics.ListAPIView):
    queryset = favorite.objects.all()
    serializer_class = FavoriteSerializer
    pagination_class = SelfPagination
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    search_fields = ('=user__id', )
    filter_class = FavoriteFilter


class FavoriteCreateView(generics.CreateAPIView):
    serializer_class = FavoriteCreateSerializer

    def post(self, request, *args, **kwargs):
        good_id = request.data.get('good')
        user_id = request.data.get('user')
        try:
            Favorite = favorite.objects.filter(good_id=good_id).filter(user_id=user_id)
        except:
            return Response(data={'code': 400, 'detail': '请先登录'}, status=status.HTTP_400_BAD_REQUEST)
        if Favorite.exists():
            serializer = FavoriteUpdateSerializer()
            serializer.update(instance=Favorite[0], validated_data={'good_num': Favorite[0].good_num + request.data.get('good_num')})
            return Response(data={'code': 201, 'detail': '创建成功'}, status=status.HTTP_201_CREATED)
        else:
            serializer = FavoriteUpdateSerializer(data=request.data)
            if serializer.is_valid():
                good = goods.objects.get(id=request.data.get("good"))
                if good.good_num <= 0:
                    return Response(data={'code': 400, 'detail': '参数错误'}, status=status.HTTP_400_BAD_REQUEST)
                serializer.save()
            else:
                return Response(data={'code': 400, 'detail': '参数错误'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data={'code': 201, 'detail': '创建成功'}, status=status.HTTP_201_CREATED)

class FavoriteUpdateView(generics.GenericAPIView):
    serializer_class = FavoriteUpdateSerializer
    def post(self, request):
        try:
            instance = favorite.objects.filter(id=request.data.get('id'))[0]
        except:
            return Response(data={'code': 400, 'detail': '商品id不存在'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = FavoriteUpdateSerializer()
        serializer.update(instance=instance,
                          validated_data={'good_num': request.data.get('good_num')})
        return Response(data={'code': 201, 'detail': '修改成功'}, status=status.HTTP_200_OK)

class FavoriteDeleteView(views.APIView):
    def post(self, request):
        favorite_id = request.data.get('id')
        if favorite_id is None:
            return Response(data={'code': 400, 'detail': '参数错误'}, status=status.HTTP_400_BAD_REQUEST)
        Favorite = favorite.objects.filter(id=favorite_id)
        if Favorite.exists():
            Favorite.delete()
            return Response(data={'code': 200, 'detail': '删除成功'}, status=status.HTTP_200_OK)
        else:
            return Response(data={'code': 400, 'detail': '商品不存在'}, status=status.HTTP_400_BAD_REQUEST)

class OrderCreateView(generics.CreateAPIView):
    serializer_class = orderCreateSerializer

    def post(self, request, *args, **kwargs):
        favorite_id = request.data.get('id')
        print(favorite_id)
        try:
            address = userAddress.objects.get(id=request.data.get("order_address"))
        except:
            return Response(data={'code': 400, 'detail': '订单创建失败'}, status=status.HTTP_400_BAD_REQUEST)
        phone = address.phone
        aceptman = address.name
        order_num = request.data.get("order_num")
        for i in favorite_id:
            Favorite = favorite.objects.filter(id=i)[0]
            good = goods.objects.get(id=Favorite.good.id)
            if good.good_num - Favorite.good_num < 0:
                return Response(data={'code': 400, 'detail': '购买失败，请重试'}, status=status.HTTP_400_BAD_REQUEST)
        for i in favorite_id:
            try:
                Favorite = favorite.objects.filter(id=i)[0]
            except:
                return Response(data={'code': 400, 'detail': '购物车为空'}, status=status.HTTP_400_BAD_REQUEST)
            good = goods.objects.get(id=Favorite.good.id)
            serializer = GoodUpdateSerializer()
            print("order_num", order_num)
            serializer.update(instance=good, validated_data={'id': good.id, 'good_num': good.good_num - Favorite.good_num})
            serializer = orderCreateSerializer(data={'good': Favorite.good.id, 'user': Favorite.user.id,
                                                     'good_num': Favorite.good_num,
                                                     'order_address': address.content, 'order_num': order_num,
                                                     "order_aceptman": aceptman, "order_phone": phone,
                                                     "order_status": 0})
            print("ok")
            good.good_num -= Favorite.good_num
            good.save()
            if serializer.is_valid():
                serializer.save()
                Favorite.delete()
        return Response(data={'code': 200, 'detail': '订单创建成功'}, status=status.HTTP_200_OK)

class alipayView(views.APIView):

    def post(self, request):
        alipay = AliPay(
            appid="2016092900622837",
            app_notify_url=None,  # 默认回调url
            app_private_key_path="./wish/private_key.txt",
            # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            alipay_public_key_path="./wish/alipay_public_key.txt",
            sign_type="RSA", # RSA 或者 RSA2
        debug = False,  # 默认False
        )
        subject = "电子产品虚拟订单"
        order_string = alipay.api_alipay_trade_page_pay(
            out_trade_no=request.data.get("order_num"),
            total_amount=request.data.get("max_price"),
            subject=subject,
            return_url="https://www.baidu.com",
            notify_url="120.78.197.127:9997/goods/test/"  # 可选, 不填则使用默认notify url
        )

        return Response(data={"code": 200, "url": "https://openapi.alipaydev.com/gateway.do?" + order_string})

class testView(views.APIView):
    def post(self,request):
        print(request.data)
        return Response(data={"code": 200})

class OrderListView(views.APIView):
    serializer_class = orderSerializer
    queryset = order.objects.all()
    filter_class = OrderFilter
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    search_fields = ('=user__id', )
    schema = OrderSchema

    def get(self, request):
        order_num = []
        num = request.query_params.get("order_num")
        if request.query_params.get("user_id") is not None:
            if request.query_params.get("order_status") is not None:
                order_list = queryset = order.objects.all().filter(
                    user_id=request.query_params.get("user_id"))\
                    .filter(order_status=request.query_params.get("order_status"))\
                    .order_by ("-order_num")
            else:
                order_list = queryset = order.objects.all().filter(user_id=request.query_params.get("user_id")).order_by("-order_num")
        else:
            if request.query_params.get("order_status") is not None:
                order_list = queryset = order.objects.all()\
                    .filter(order_status=request.query_params.get("order_status"))\
                    .order_by ("-order_num")
            else:
                order_list = queryset = order.objects.all().filter().order_by ("-order_num")
        if num is not None:
            order_list = order_list.filter(order_num=num)
        for i in order_list:
            if int(i.order_num) in order_num:
                pass
            else:
                order_num.append(int(i.order_num))
        order_num.sort(reverse=True)
        result = []
        for i in order_num:
            tmp = order_list.filter(order_num=i)
            user = User.objects.get(id=tmp[0].user_id)
            data = {"order_num": str(i), "order_time":tmp[0].order_time, "data": [], "max_price": 0,
                    "order_address": tmp[0].order_address, "order_aceptman": tmp[0].order_aceptman,
                    "order_phone": tmp[0].order_phone, "order_status": tmp[0].order_status,
                    "user_name": user.username
                    }
            good_max_price = 0
            for y in tmp:
                good = goods.objects.get(id=y.good_id)
                o = {"id": y.id, "good_num": y.good_num, "good_id": y.good_id, "good_img": good.good_img.name,
                     "good_name": good.good_name, "good_price": good.good_price}
                good_max_price += y.good_num * good.good_price
                data["data"].append(o)
            result.append(data)
            data["max_price"] = good_max_price
        page = int(request.query_params.get ('page', 1))
        page_size = int(request.query_params.get ('page_size', 7))
        paginator = Paginator(result, page_size)
        if page_size != 0 and page != 0 and page_size * page - page_size >= len(result):
            return Response({'detail': '无效页面。'})
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            contacts = paginator.page(1)
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)
        data = {"count": len(result), "result": contacts.object_list}
        return Response(data)

class orderDeleteView(views.APIView):
    def post(self, request):
        order_num = request.data.get("order_num")
        order_list = order.objects.filter(order_num=order_num)
        for i in order_list:
            good = goods.objects.get(id=i.good_id)
            good.good_num += i.good_num
            good.save()
            i.delete()
        return Response(data={"code": 200, "detail": "删除成功"}, status=status.HTTP_200_OK)

class orderUpdateView(generics.GenericAPIView):
    serializer_class = orderSerializer
    queryset = order.objects.all()
    def post(self, request):
        try:
            instance = order.objects.filter(order_num=request.data.get("order_num"))
        except:
            return Response(data={"code": 400, "detail": "参数错误"}, status=status.HTTP_400_BAD_REQUEST)

        for i in instance:
            serializer = orderSerializer()
            serializer.update(instance=i, validated_data=request.data)

        return Response(data={"code": 200, "detail": "修改成功"}, status=status.HTTP_200_OK)

class CommentListView(generics.ListAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    pagination_class = SelfPagination
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filter_class = CommentFilter

class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentCreateSerializer

    def post(self, request, *args, **kwargs):
        commentSerializer = CommentCreateSerializer(data=request.data)
        if commentSerializer.is_valid():
            commentSerializer.save()
        else:
            return Response(data={"code": 400, "detail": "参数错误"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data={"code": 201, "detail": "创建成功"}, status=status.HTTP_201_CREATED)

class ReplayListView(generics.ListAPIView):
    serializer_class = ReplaySerializer
    queryset = replay.objects.all()
    pagination_class = SelfPagination
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filter_class = ReplayFilter

class ReplayCreateView(generics.CreateAPIView):
    serializer_class = ReplayCreateSerializer

    def post(self, request, *args, **kwargs):
        replaySerializer = ReplayCreateSerializer(data=request.data)
        if replaySerializer.is_valid():
            replaySerializer.save()
        else:
            return Response(data={"code": 400, "detail": "参数错误"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data={"code": 201, "detail": "创建成功"}, status=status.HTTP_201_CREATED)

class GoodTypeListView(generics.ListAPIView):
    serializer_class = GoodTypeSerializer
    queryset = goods_type.objects.all()
    pagination_class = SelfPagination
    filter_backends = (filters.SearchFilter)
    filter_class = GoodTypeFilter
