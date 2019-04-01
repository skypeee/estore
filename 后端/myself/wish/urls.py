from django.conf.urls import url, include
from wish import views
from rest_framework_jwt.views import verify_jwt_token, obtain_jwt_token

from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
schema_view = get_schema_view(title='Users API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

urlpatterns = [
    url(r'^api-token-verify/', verify_jwt_token),
    url(r'file_download/', views.file_download.as_view(), name='user_download'),


]
