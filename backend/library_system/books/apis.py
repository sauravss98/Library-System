from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView
)
from django.contrib.auth import get_user_model
from .models import Book
from .serializers import BookSerializer


class CreateBookDetailsView(CreateAPIView):
    serializer_class = BookSerializer

class BooksListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
class BookListView(RetrieveAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class UpdateBookDetailsView(UpdateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class DeleteBookView(DestroyAPIView):
    queryset = Book.objects.all()