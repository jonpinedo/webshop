from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cart, CartItem
from .serializers import CartSerializer


@api_view(['POST'])
def create_cart(request):
    # Obtener los datos del request
    item_id = request.data.get('item_id')
    country_code = request.data.get('country_code')

    # Validar los datos
    if not item_id or not country_code:
        return Response({'message': 'Invalid data'}, status=400)

    # Crear un nuevo carro
    cart = Cart.objects.create(country_code=country_code)

    # Agregar el item al carro
    cart.items.add(item_id)

    # Devolver el identificador del carro creado
    return Response({'cart_id': cart.id}, status=201)



@api_view(['GET'])
def get_cart_content(request):
    #obtener los datos del request
    cart_id = request.query_params.get("cart_id")

    try:
        cart = Cart.objects.get(id=cart_id)
    except Cart.DoesNotExist:
        return Response({'message': 'Cart not found'})
    
    
    serializer = CartSerializer(cart)
    return Response(serializer.data, status=200)
