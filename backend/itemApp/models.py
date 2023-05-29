from django.db import models

class Item(models.Model):
    """Model for the items (articles) including id, name, price and image"""
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=100)
    item_price = models.DecimalField(max_digits=8, decimal_places=2)
    item_image = models.ImageField(upload_to='item_images')

    def __str__(self):
        return self.item_name