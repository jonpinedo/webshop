from django.contrib import admin
from .models import Cart, CartItem

# Register your models here.
@admin.register(Cart)
class ItemAdmin(admin.ModelAdmin):
    pass

@admin.register(CartItem)
class ItemAdmin(admin.ModelAdmin):
    pass
