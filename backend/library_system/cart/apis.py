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
from .serializers import CartSerializer, CartCreateSerializer

class AddToCartView(CreateAPIView):
    serializer_class = CartCreateSerializer
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CartItemList(ListAPIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CartSerializer
    def get_queryset(self):
        queryset = Cart.objects.all()
        return queryset