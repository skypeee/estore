from rest_framework.generics import ListAPIView
from django.contrib.auth import get_user_model
from random import randint
from twilio.rest import Client
from django.http import FileResponse
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import views
# Create your views here.
User = get_user_model()


class file_download(views.APIView):
    def post(self, request):
        file = open(r'C:\Users\skypee\Desktop\2.mp4', 'rb')
        response = FileResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="2.mp4'
        print('ok')
        return response


