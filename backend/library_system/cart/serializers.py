from rest_framework import serializers
from .models import Cart
from user.models import User
from books.serializers import BookSerializer

# class CartSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Cart
#         fields = ["__all__"]

# class CartCreateSerializer(serializers.ModelSerializer):
#     books = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

#     class Meta:
#         model = Cart
#         fields = ["user","books"]
    
class CartItemSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'books',]

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'created_at']