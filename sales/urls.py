# This file is temporarily disabled
"""
from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'sales'

urlpatterns = [
    path('', views.sales, name='sales'),
    path('order_list/', views.order_list, name='order_list'),
    path('create/', views.order_create, name='order_create'),
    path('<int:pk>/', views.order_detail, name='order_detail'),
    path('<int:pk>/update/', views.order_update, name='order_update'),
    path('<int:pk>/delete/', views.order_delete, name='order_delete'),
]
"""