# Temporarily commented out
"""
from django.db import models
from django.conf import settings
from products.models import Product

class ProductReport(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Product Report - {self.product.name}"

class InventoryReport(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField()
    total_products = models.IntegerField()
    total_value = models.DecimalField(max_digits=10, decimal_places=2)
    low_stock_items = models.IntegerField()
    out_of_stock_items = models.IntegerField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Inventory Report - {self.date}"
"""
