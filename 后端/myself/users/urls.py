from django.conf.urls import url, include
from users import views
from rest_framework_jwt.views import verify_jwt_token, obtain_jwt_token

urlpatterns = [
    url(r'User_List/', views.UserListView.as_view(), name='user_list'),
    url(r'User_Created/', views.UserCreateView.as_view(), name='user_created'),
    url(r'User_Updated/', views.UserUpdateView.as_view(), name='user_update'),
    url(r'message_send/', views.message_sendView.as_view(), name='message_send'),
    url(r'^api-token-auth/', obtain_jwt_token),
]
