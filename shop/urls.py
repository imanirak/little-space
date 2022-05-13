from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('user/<username>', views.profile, name='profile'),
     #SHOP
    path('shop/new', views.Shop_Create.as_view(), name="shop_create"),
    path('shop/', views.Shop_List.as_view(), name="shop_list"),
    path('shop/<int:pk>/', views.Shop_Detail.as_view(), name="shop_detail"),
    path('shop/<int:device_id>', views.Shop_Show, name='shop_show'),
    path('shop/<int:pk>/update', views.Shop_Update.as_view(), name="shop_update"),
    path('shop/<int:pk>/delete', views.Shop_Delete.as_view(), name="shop_delete"),
    #Inventory 
    path('inventory/new', views.Inventory_Create.as_view(), name="inventory_create"),
    path('inventory/', views.Inventory_List.as_view(), name="inventory_list"),
    path('inventory/<int:pk>/', views.Inventory_Detail.as_view(), name="inventory_detail"),
    path('inventory/<int:device_id>', views.Inventory_Show, name='inventory_show'),
    path('inventory/<int:pk>/update', views.Inventory_Update.as_view(), name="inventory_update"),
    path('inventory/<int:pk>/delete', views.Inventory_Delete.as_view(), name="inventory_delete"),
    #AUTH
    path('accounts/signup/', views.signup_view, name="signup")

]