from django.conf.urls import url, include
from goods import views
urlpatterns = [
    url(r'Good_Create/', views.GoodCreateView.as_view(), name='good_create'),
    url(r'Good_list/', views.GoodListView.as_view(), name='good_list'),
    url(r'Good_Delete/', views.GoodDeleteView.as_view(), name='good_delete'),
    url(r'Good_Update/', views.GoodUpdateView.as_view(), name='good_update'),
    url(r'Favorite_List/', views.FavoriteListView.as_view(), name='Favorite_List'),
    url(r'Favorite_Create/', views.FavoriteCreateView.as_view(), name='Favorite_List'),
    url(r'Favorite_Update/', views.FavoriteUpdateView.as_view(), name='Favorite_update'),
    url(r'Favorite_Delete/', views.FavoriteDeleteView.as_view(), name='Favorite_Delete'),
    url(r'Border_Created/', views.OrderCreateView.as_view(), name='Order_Create'),
    url(r'Order_List/', views.OrderListView.as_view(), name="Order_List"),
]