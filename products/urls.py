from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'products'

urlpatterns = [
    path('our_products/', views.our_products, name='our_products'),
    path('inventory/', views.inventory, name='inventory'),
    path('create/', views.product_create, name='product_create'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('<int:pk>/update/', views.product_update, name='product_update'),
    path('<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('<int:pk>/buy/', views.buy_now, name='buy_now'),
    path('my_orders/', views.my_orders, name='my_orders'),
    path('all_orders/', views.all_orders, name='all_orders'),
    path('order/<int:order_id>/update/', views.update_order_status, name='update_order_status'),
    path('order/<int:order_id>/delete/', views.order_delete, name='order_delete'),
    path('purchase_success/<int:pk>/', views.purchase_success, name='purchase_success'),
]