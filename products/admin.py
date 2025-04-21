from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock_quantity', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'description')
    ordering = ('-created_at',)
