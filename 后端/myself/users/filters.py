import django_filters
from .models import userAddress

class AddressFilter(django_filters.rest_framework.FilterSet):
    id = django_filters.CharFilter(field_name="id")

    class Meta:
        model = userAddress
        fields = ["id",]