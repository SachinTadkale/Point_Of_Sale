from django.db import models
from django.core.validators import MinValueValidator # type: ignore
from django.conf import settings

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    stock_quantity = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('delivered', 'Delivered'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.product.name} - {self.status}"
