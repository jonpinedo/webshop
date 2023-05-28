from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    
    def get_image(self, item):
        request = self.context['request']
        absolute_image_uri = request.build_absolute_uri(item.item_image.url)
        return absolute_image_uri

    class Meta:
        model = Item
        fields = ('item_id', 'item_name', 'item_price', 'image')
