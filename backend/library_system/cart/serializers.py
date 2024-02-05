from rest_framework import serializers
from .models import Cart
from user.models import User

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ["__all__"]

class CartCreateSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ["user","books"]
    
