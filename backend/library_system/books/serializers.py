from rest_framework import serializers
from .models import *

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for Books
    """
    class Meta:
        model = Book
        fields = ['id','title', 'author_name', 'quantity']
