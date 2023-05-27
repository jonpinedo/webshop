from rest_framework import viewsets
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer
from rest_framework.decorators import api_view

"""
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
"""

@api_view(['GET'])
def get_items(request):
    #obtener los datos del request
    
    try:
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True, context={"request": request})
        return Response(serializer.data, status=200)
    except Item.DoesNotExist:
        return Response({'message': 'No items found'})