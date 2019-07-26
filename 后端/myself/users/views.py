from rest_framework.generics import ListAPIView
from .serializers import UserSerializer, UserUpdateSerializer, addressSerializer, addressDeleteSerializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status, generics, filters
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import views
from random import randint
from .filters import AddressFilter
from twilio.rest import Client
from django.shortcuts import render
from .models import userAddress
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination


class SelfPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100

# Create your views here.
User = get_user_model()


# Create your views here.

class UserListView(ListAPIView):
    """
    获取用户列表接口
    
    """
    serializer_class = UserSerializer
    queryset = User.objects.filter()
    search_fields = ('=id', )
    filter_backends = (filters.SearchFilter, )

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'code': 400, 'detail': '创建失败'}, status=status.HTTP_400_BAD_REQUEST)
        new_user = serializer.save()
        return Response(data={'code': 200, 'detail': '创建成功'}, status=status.HTTP_201_CREATED)

class UserUpdateView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer

    def get_object(self):
        user_id = self.kwargs.get('user_id', None)
        if user_id is None:
            return Response(data={'code': 400, 'detail': '缺少用户ID'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            obj = User.objects.get(id=user_id)
        except:
            return Response(data={'code': 400, 'detail': '用户不存在'}, status=status.HTTP_404_NOT_FOUND)
        return obj

    def post(self, request, *args, **kwargs):
        user_id = request.data.get('id', None)
        if user_id is not None:
            self.kwargs.update({'user_id': user_id})
        instance = self.get_object()
        data = request.data.copy()
        try:
            password = data.pop("password")
            instance.set_password (password)
        except:
            pass
        serializer = self.get_serializer(instance, data=data, partial=True)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response(data={'code': 400, 'detail': '修改失败'}, status=status.HTTP_400_BAD_REQUEST)
        serializer.update(instance=instance, validated_data=data)
        return Response(data={'code': 200, 'detail': '更新成功'}, status=status.HTTP_200_OK)

class message_sendView(views.APIView):
    def post(self, request):
        phone_num = request.data.get('phone_num')
        account_sid = "AC2963fc2f673bb385617ed24d335e336c"
        auth_token = "0e259f69dae3474889f36f62189c9770"
        client = Client(account_sid, auth_token)
        CAPTCHA = randint(1000, 10000)
        message = client.messages.create(
            to="+86" + phone_num,
            from_="+19389999241",
            body="Hello from Python Twilio! Your captcha is {}".format(CAPTCHA))
        return Response(data={'code': 200, 'detail': '发送成功', 'CAPTCHA': CAPTCHA})

class addressListView(ListAPIView):
    queryset = userAddress.objects.all()
    serializer_class = addressSerializer
    pagination_class = SelfPagination
    search_fields = ('=user__id', )
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filter_class = AddressFilter


class addressCreateView(generics.CreateAPIView):
    queryset = userAddress.objects.all()
    serializer_class = addressSerializer
    def post(self, request, *args, **kwargs):
        serializer = addressSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'code': 400, 'detail': '创建失败'}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(data={'code': 200, 'detail': '创建成功'}, status=status.HTTP_201_CREATED)

class addressDeleteView(generics.GenericAPIView):

    queryset = userAddress.objects.all()
    serializer_class = addressDeleteSerializer
    def post(self, request, *args, **kwargs):
        try:
            address = userAddress.objects.get(id=request.data.get("id"))
        except:
            return Response (data={'code': 400, 'detail': '删除失败'}, status=status.HTTP_400_BAD_REQUEST)
        address.delete()
        return Response(data={'code': 200, 'detail': '删除成功'}, status=status.HTTP_201_CREATED)

class addressUpdateView(generics.GenericAPIView):
    queryset = userAddress.objects.all()
    serializer_class = addressSerializer
    def post(self, request, *args, **kwargs):
        id = request.data.get("id")
        try:
            address = userAddress.objects.get(id=id)
            user = User.objects.get(id=request.data.get("user"))
        except:
            return Response (data={'code': 400, 'detail': '更新失败'}, status=status.HTTP_400_BAD_REQUEST)
        data = request.data.copy()
        data["user"] = user
        try:
            serializer = addressSerializer()
            serializer.update(instance=address, validated_data=data)
        except:
            return Response (data={'code': 400, 'detail': '更新失败'}, status=status.HTTP_400_BAD_REQUEST)
        return Response (data={'code': 200, 'detail': '更新成功'}, status=status.HTTP_200_OK)


