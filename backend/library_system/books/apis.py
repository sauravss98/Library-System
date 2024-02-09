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
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import SessionAuthentication,TokenAuthentication


class CreateBookDetailsView(CreateAPIView):
    """
    Api view to create the book details
    """
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = BookSerializer

class BooksListView(ListAPIView):
    """
    Api view to create the book list
    """
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        return queryset
    
class BookListView(RetrieveAPIView):
    """
    Api view to list the book details
    """
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer
    def get_queryset(self):
        queryset = Book.objects.all()
        return queryset

class UpdateBookDetailsView(UpdateAPIView):
    """
    Api view to update the book details
    """
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = BookSerializer
    def get_queryset(self):
        queryset = Book.objects.all()
        return queryset

class DeleteBookView(DestroyAPIView):
    """
    Api view to delete the book details
    """
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Book.objects.all()
