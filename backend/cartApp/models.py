from django.db import models
from itemApp.models import Item
from django.contrib.auth.models import User
import decimal

class CountryCode:
    ES = 'es'
    EN = 'en'
    CHOICES = [
        (ES, 'spanish'),
        (EN, 'english'),
    ]


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country_code = models.CharField(max_length=10, choices=CountryCode.CHOICES)
    items = models.ManyToManyField(Item, through='CartItem')

    @property
    def price(self):
        """Returns the total price of the cart"""
        result = decimal.Decimal(0.0)
        for cart_item in CartItem.objects.filter(cart=self):
            result += cart_item.total_price
        return result

    def __str__(self):
        return f"Cart ({self.id}) - {self.country_code}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    @property
    def total_price(self):
        """Returns the total price of the CartItem"""
        return self.quantity * self.item.item_price

    def __str__(self):
        return f"{self.item.item_name} - Quantity: {self.quantity}"
