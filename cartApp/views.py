from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .models import Cart
from .serializers import CartDetailSerializer, CartCheckoutSerializer
from django.contrib.auth.models import User



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
        user_id = request.user.id or 2
        serializer = CartCheckoutSerializer(data=request.data, context={"user_id": user_id})
        if serializer.is_valid():
            cart_id = serializer.create(serializer.data)
            return Response({"cart_id": cart_id})
        else:
            return Response(serializer.errors)


# Vista para realizar el login y obtener el token de autenticación
class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

# Vista para realizar el logout y eliminar el token de autenticación
class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response({'detail': 'Logout successful'})
