import ast
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView
)
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Cart
# from .serializers import CartSerializer, CartCreateSerializer

# class AddToCartView(CreateAPIView):
#     serializer_class = CartCreateSerializer
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class CartItemList(ListAPIView):
#     authentication_classes = [SessionAuthentication, TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#     serializer_class = CartSerializer
#     def get_queryset(self):
#         queryset = Cart.objects.all()
#         return queryset

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Cart, CartItem, Book
from .serializers import CartSerializer, CartItemSerializer

class AddToCart(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        book_ids = request.data.get('book_ids', [])
        input_string = "[1,2,3,4]"
        book_ids = ast.literal_eval(input_string)
        user = request.user
        cart, _ = Cart.objects.get_or_create(user=user)
        print(book_ids)
        for book_id in book_ids:
            print(book_id)
            try:
                book = Book.objects.get(pk=book_id)
                print(book)
                cart_item, _ = CartItem.objects.get_or_create(cart=cart)
                cart_item.books.add(book)
            except Book.DoesNotExist:
                pass  # You might want to handle this case if needed
        
        serializer = CartSerializer(cart)
        return Response(serializer.data)

class ViewCart(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        print(user)
        cart= Cart.objects.get(user=user)
        print(cart)
        cart_item = CartItem.objects.get(cart = cart)
        print(cart)
        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data)

class ModifyCart(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, cart_item_id, book_id):
        try:
            cart_item = CartItem.objects.get(pk=cart_item_id)
            book = Book.objects.get(pk=book_id)
            cart_item.books.remove(book)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except (CartItem.DoesNotExist, Book.DoesNotExist):
            return Response({"error": "Cart item or book does not exist"}, status=status.HTTP_404_NOT_FOUND)

class Checkout(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        cart, _ = Cart.objects.get_or_create(user=user)
        for cart_item in cart.cartitem_set.all():
            for book in cart_item.books.all():
                book.quantity -= 1
                book.save()
        # Logic for checking out the cart
        # You can implement payment processing, order creation, etc.
        # After checking out, you may want to clear the cart
        cart.delete()
        return Response({"message": "Checkout successful"})