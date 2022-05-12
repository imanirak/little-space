from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name="home"),
     #SHOP
    path('shop/new', views.Shop_Create.as_view(), name="shop_create"),
    path('shop/', views.Shop_List.as_view(), name="shop_list"),
    path('shop/<int:pk>/', views.Shop_Detail.as_view(), name="shop_detail"),
    path('shop/<int:pk>/update', views.Shop_Update.as_view(), name="shop_update"),
    path('shop/<int:pk>/delete', views.Shop_Delete.as_view(), name="shop_delete"),

]