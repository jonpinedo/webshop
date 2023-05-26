from django.db import models
from itemApp.models import Item

# Create your models here.
class Cart(models.Model):
    country_code = models.CharField(max_length=10)
    items = models.ManyToManyField(Item, through='CartItem')

    def __str__(self):
        return f"Cart ({self.id}) - {self.country_code}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.item.item_name} - Quantity: {self.quantity}"
