from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Sum, F

# Create your models here.

class Customer(AbstractUser): 
    DEPARTMENT_CHOICES = [
        ('comum', 'Comum'),
        ('membro', 'Membro'),
    ]

    department = models.CharField(
        max_length=10,
        choices=DEPARTMENT_CHOICES,
        default='comum',  # opcional: valor padrão
        blank=True,
        null=True
    )

    def __str__(self): 
        return self.get_full_name() or self.username




class Product(models.Model): 
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self): 
        return self.name




class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField(
        auto_now_add=True, 
        db_comment='Date and time when the purchase was made.'
        )

    @property
    def total_price(self):
        return self.items.aggregate(
            total = Sum(F('unit_price') * F('quantity'))
        )['total'] or 0

    def __str__(self):
        return f'Order number: {self.id} client: {self.customer} date: {self.order_date}'




class OrderItem(models.Model): 
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        if not self.unit_price:
            self.unit_price = self.product.price
        super().save(*args, **kwargs)




class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    last_update = models.DateField()




class Cart(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    
    def total_items(self):
        return sum(item.quantity for item in self.cartitem_set.all())

    def total_price(self):
        return sum(item.product.price * item.quantity for item in self.cartitem_set.all())




class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.unit_price:
            self.unit_price = self.product.price
        super().save(*args, **kwargs)