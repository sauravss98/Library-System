from django.urls import path
# from .apis import (
#     BooksListView, 
#     CreateBookDetailsView,
#     BookListView,
#     UpdateBookDetailsView,
#     DeleteBookView
# )
from .views import signup,login,test_token

urlpatterns = [ 
        path('signup', signup),
        path('login', login),
        path('test_token', test_token),
]
# urlpatterns = [
#     path('create/', CreateBookDetailsView.as_view()),
#     path('list/', BooksListView.as_view()),
#     path('<int:pk>/',BookListView.as_view()),
#     path('update/<int:pk>/',UpdateBookDetailsView.as_view()),
#     path('delete/<int:pk>/',DeleteBookView.as_view()),
# ]