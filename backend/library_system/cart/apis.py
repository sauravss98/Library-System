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
    """
    Api to add item to cart
    """
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        book_ids = request.data.get('book_ids', [])
        print(type(book_ids))
        book_ids_array = []
        book_ids_array.append(book_ids)
        user = request.user
        cart, _ = Cart.objects.get_or_create(user=user)
        print(book_ids)
        for book_id in book_ids_array:
            print(book_id)
            try:
                book = Book.objects.get(pk=book_id)
                print(book)
                cart_item, _ = CartItem.objects.get_or_create(cart=cart)
                cart_item.books.add(book)
            except Book.DoesNotExist:
                pass        
        serializer = CartSerializer(cart)
        return Response(serializer.data)

class ViewCart(APIView):
    """
    Api to view item in cart
    """
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
    
class CartCount(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        count = 0
        user = request.user
        cart= Cart.objects.get(user=user)
        cart_item = CartItem.objects.get(cart = cart)
        serializer = CartItemSerializer(cart_item)
        items = serializer.data
        books = items["books"]
        print(books)
        for book in books:
            print(book)
            count+=1
        # count = serializer.data.count
        # print("Count is "+count)
        return Response({"count":count})
        # return Response(count)



class ModifyCart(APIView):
    """
    Api to edit item in cart
    """
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
    """
    Api to checkout in cart
    """
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