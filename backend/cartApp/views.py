from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Cart
from .serializers import CartDetailSerializer, CartCheckoutSerializer


class CartDetail(APIView):
    def get(self, request, id):
        """Gets detail of a cart given an ID"""

        try:
            cart = Cart.objects.get(id=id)
            serializer = CartDetailSerializer(cart, context={"request": request})
            return Response(serializer.data, status=200)
        except Cart.DoesNotExist:
            return Response({'message': 'Cart not found'})


class CartCheckout(APIView):
    def post(self, request, *args, **kwargs):
        user_id = request.user.id
        serializer = CartCheckoutSerializer(data=request.data, context={"user_id": user_id})
        if serializer.is_valid():
            cart_id = serializer.create(serializer.data)
            return Response({"cart_id": cart_id})
        else:
            return Response(serializer.errors)

