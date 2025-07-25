from django.db import models
from django.core.validators import MinValueValidator
from users.models import User
from products.models import Product

class Order(models.Model):
    PENDING = 'P'
    SHIPPED = 'S'
    DELIVERED = 'D'
    
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (SHIPPED, 'Shipped'),
        (DELIVERED, 'Delivered'),
    ]
    
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Order #{self.id} - {self.user.email}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order #{self.order.id}"