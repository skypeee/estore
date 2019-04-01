from django.shortcuts import render
from .serializers import goodCreateSerializer, goodSerializer, GoodUpdateSerializer, FavoriteSerializer, orderCreateSerializer\
    , FavoriteUpdateSerializer, FavoriteCreateSerializer, orderSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import status, generics, views, filters
from rest_framework.response import Response
from .models import goods, favorite, order
from django.contrib.auth import get_user_model
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
    search_fields = ('=id', '=good_type', 'good_brand', 'good_name', 'good_content')
    filter_backends = (filters.SearchFilter, )

class GoodCreateView(generics.CreateAPIView):
    serializer_class = goodCreateSerializer

    def post(self, request, *args, **kwargs):
        GoodSerializer = goodCreateSerializer(data=request.data)
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
    filter_backends = (filters.SearchFilter, )
    search_fields = ('=user__id', )

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
                          validated_data={'good_num': instance.good_num + request.data.get('good_num')})
        return Response(data={'code': 201, 'detail': '创建成功'}, status=status.HTTP_201_CREATED)

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
        for i in favorite_id:
            Favorite = favorite.objects.filter(id=i)[0]
            # try:
            good = goods.objects.get(id=Favorite.good.id)
            serializer = GoodUpdateSerializer()
            serializer.update(instance=good, validated_data={'id': good.id, 'good_num': good.good_num - Favorite.good_num})
            serializer = orderCreateSerializer(data={'good': Favorite.good.id, 'user': Favorite.user.id, 'good_num': Favorite.good_num,
                                                     'order_address': '123'})
            # 'order_address': Favorite.user.user_address})
            if serializer.is_valid():
                serializer.save()
            Favorite.delete()
        return Response(data={'code': 200, 'detail': '购买成功'}, status=status.HTTP_200_OK)

class OrderListView(generics.ListAPIView):
    serializer_class = orderSerializer
    queryset = order.objects.all()
    pagination_class = SelfPagination
    filter_backends = (filters.SearchFilter, )
    search_fields = ('=user__id', )
