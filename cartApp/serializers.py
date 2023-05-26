from rest_framework import serializers
from .models import Cart, CartItem
from itemApp.serializers import ItemSerializer


class CartItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer(required=False, read_only=True, source='*')  

    class Meta:
        model = CartItem
        fields = ['id', 'item', 'quantity']




class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)  

    class Meta:
        model = Cart
        fields = ('id', 'country_code', 'items')

