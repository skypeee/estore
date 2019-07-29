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
    url(r'Order_Delete/', views.orderDeleteView.as_view(), name="Order_Delete"),
    url(r"Comment_List/", views.CommentListView.as_view(), name="Comment_List"),
    url(r"Comment_Created/", views.CommentCreateView.as_view(), name="Comment_List"),
    url(r"Order_Update/", views.orderUpdateView.as_view(), name="order_update"),
    url(r"ali_Pay/", views.alipayView.as_view(), name="aliPay"),
    url(r"replay_List/", views.ReplayListView.as_view(), name="replay_list"),
    url(r"relay_Created/", views.ReplayCreateView.as_view(), name="replay_created"),
    url(r"test/", views.testView.as_view(), name="test"),
    url(r"GoodType_List/", views.GoodTypeListView.as_view(), name="goodType_list"),
]
