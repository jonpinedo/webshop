from rest_framework import serializers
from .models import Cart, CartItem, CountryCode
from itemApp.serializers import ItemSerializer
from itemApp.models import Item
from django.db import transaction


class CartItemSerializer(serializers.Serializer):
    item = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all())
    quantity = serializers.IntegerField()
    
    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError('Quantity must be > 0')
        return value
    
    class Meta:
        fields = ['item', 'quantity']


class CartCheckoutSerializer(serializers.Serializer):
    items = CartItemSerializer(many=True)
    country_code = serializers.ChoiceField(choices=CountryCode.CHOICES)

    class Meta:
        fields = ('country_code', 'items')

    @transaction.atomic
    def create(self, validated_data):
        user_id = self.context["user_id"]
        country_code = validated_data.get("country_code")
        items = validated_data.get("items")
        cart_obj = Cart.objects.create(
            user_id=user_id,
            country_code=country_code,
        )
        for item in items:
            cart_item = CartItem.objects.create(
                item_id=item["item"],
                quantity=item["quantity"],
                cart_id=cart_obj.id,
            )
        return cart_obj.id


class CartItemDetailSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True, source='item.item_id')
    name = serializers.CharField(read_only=True, source='item.item_name')
    quantity = serializers.CharField(read_only=True)
    price = serializers.DecimalField(read_only=True, source='item.item_price', max_digits=10, decimal_places=2)
    total_price = serializers.CharField(read_only=True)
    image = serializers.SerializerMethodField()

    def get_image(self, cart_item):
        request = self.context['request']
        complete_uri = request.build_absolute_uri(cart_item.item.item_image.url)
        return complete_uri

    class Meta:
        model = CartItem
        fields = [
            'id',
            'name',
            'quantity',
            'price',
            'total_price',
            'image',
        ]


class CartDetailSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
    country_code = serializers.ChoiceField(choices=CountryCode.CHOICES, read_only=True)
    price = serializers.CharField(read_only=True)

    def get_items(self, cart):
        queryset = CartItem.objects.filter(cart=cart)
        return CartItemDetailSerializer(queryset, many=True, context=self.context).data

    class Meta:
        depth = 1
        model = Cart
        fields = ('id', 'country_code', 'items', 'price')

