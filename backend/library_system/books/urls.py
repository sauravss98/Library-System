from django.urls import path
from .apis import (
    BooksListView, 
    CreateBookDetailsView,
    BookListView,
    UpdateBookDetailsView,
    DeleteBookView
)


urlpatterns = [
    path('create/', CreateBookDetailsView.as_view()),
    path('list/', BooksListView.as_view()),
    path('<int:pk>/',BookListView.as_view()),
    path('update/<int:pk>/',UpdateBookDetailsView.as_view()),
    path('delete/<int:pk>/',DeleteBookView.as_view()),
]