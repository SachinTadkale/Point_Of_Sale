from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'products'

urlpatterns = [
    path('our-products/', views.our_products, name='our_products'),
    path('inventory/', views.inventory, name='inventory'),
    path('create/', views.product_create, name='product_create'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('<int:pk>/update/', views.product_update, name='product_update'),
    path('<int:pk>/delete/', views.product_delete, name='product_delete'),
]