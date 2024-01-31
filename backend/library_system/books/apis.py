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
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        return queryset
    
class BookListView(RetrieveAPIView):
    serializer_class = BookSerializer
    def get_queryset(self):
        queryset = Book.objects.all()
        return queryset

class UpdateBookDetailsView(UpdateAPIView):
    serializer_class = BookSerializer
    def get_queryset(self):
        queryset = Book.objects.all()
        return queryset

class DeleteBookView(DestroyAPIView):
    queryset = Book.objects.all()