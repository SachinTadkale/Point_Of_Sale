from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'reports'

# Temporarily commented out
"""
urlpatterns = [
    path('', views.reports_dashboard, name='dashboard'),
    path('sales/generate/', views.generate_sales_report, name='generate_sales_report'),
    path('sales/<int:pk>/', views.sales_report_detail, name='sales_report_detail'),
    path('products/generate/', views.generate_product_report, name='generate_product_report'),
    path('products/<int:pk>/', views.product_report_detail, name='product_report_detail'),
    path('inventory/generate/', views.generate_inventory_report, name='generate_inventory_report'),
    path('inventory/<int:pk>/', views.inventory_report_detail, name='inventory_report_detail'),
]
"""