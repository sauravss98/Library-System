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
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = BookSerializer

class BooksListView(ListAPIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        return queryset
    
class BookListView(RetrieveAPIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer
    def get_queryset(self):
        queryset = Book.objects.all()
        return queryset

class UpdateBookDetailsView(UpdateAPIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = BookSerializer
    def get_queryset(self):
        queryset = Book.objects.all()
        return queryset

class DeleteBookView(DestroyAPIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Book.objects.all()