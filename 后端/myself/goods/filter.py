import django_filters
from .models import goods, Comment, order, replay, favorite

class GoodFilter(django_filters.rest_framework.FilterSet):
    id = django_filters.CharFilter(field_name="id")

    class Meta:
        model = goods
        fields = ["id",]

class CommentFilter(django_filters.rest_framework.FilterSet):
    id = django_filters.CharFilter(field_name="id")
    good_id = django_filters.CharFilter(field_name="good_id")
    user_id = django_filters.CharFilter(field_name="user_id")

    class Meta:
        model = Comment
        fields = ["id", "good_id", "user_id"]

class ReplayFilter(django_filters.rest_framework.FilterSet):
    id = django_filters.CharFilter(field_name="id")
    comment_id = django_filters.CharFilter(field_name="comment_id")
    user_id = django_filters.CharFilter(field_name="user_id")

    class Meta:
        model = replay
        fields = ["id", "comment_id", "user_id"]

class OrderFilter(django_filters.rest_framework.FilterSet):
    user_id = django_filters.CharFilter(field_name="user_id")
    order_status = django_filters.CharFilter(field_name="order_status")
    order_num = django_filters.CharFilter(field_name="order_num")

    class Meta:
        model = order
        fields = ["user_id", "order_status", "order_num"]

class FavoriteFilter(django_filters.rest_framework.FilterSet):
    id = django_filters.CharFilter(field_name="id")

    class Meta:
        model = favorite
        fields = ["id"]
