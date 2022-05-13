from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('user/<username>', views.profile, name='profile'),
     #SHOP
    path('shop/new', views.Shop_Create.as_view(), name="shop_create"),
    path('shop/', views.Shop_List.as_view(), name="shop_list"),
    path('shop/<int:pk>/', views.Shop_Detail.as_view(), name="shop_detail"),
    path('shop/<int:shop_id>', views.Shop_Show, name='shop_show'),
    path('shop/<int:pk>/update', views.Shop_Update.as_view(), name="shop_update"),
    path('shop/<int:pk>/delete', views.Shop_Delete.as_view(), name="shop_delete"),
    #Inventory 
    path('inventory/new', views.Inventory_Create.as_view(), name="inventory_create"),
    path('inventory/', views.Inventory_List.as_view(), name="inventory_list"),
    path('inventory/<int:pk>/', views.Inventory_Detail.as_view(), name="inventory_detail"),
    path('inventory/<int:item_id>', views.Inventory_Show, name='inventory_show'),
    path('inventory/<int:pk>/update', views.Inventory_Update.as_view(), name="inventory_update"),
    path('inventory/<int:pk>/delete', views.Inventory_Delete.as_view(), name="inventory_delete"),
    #Item 
    path('item/new', views.Item_Create.as_view(), name="item_create"),
    path('item/', views.Item_List.as_view(), name="item_list"),
    path('item/<int:pk>/', views.Item_Detail.as_view(), name="item_detail"),
    path('item/<int:item_id>', views.Item_Show, name='item_show'),
    path('item/<int:pk>/update', views.Item_Update.as_view(), name="item_update"),
    path('item/<int:pk>/delete', views.Item_Delete.as_view(), name="item_delete"),
    #AUTH
    path('accounts/signup/', views.signup_view, name="signup")

]