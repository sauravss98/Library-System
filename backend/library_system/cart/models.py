from django.db import models
from books.models import Book
from user.models import User
# Create your models here.

class Cart(models.Model):
    """
    Models for Cart
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart for {self.user.username}"

class CartItem(models.Model):
    """
    Models for CartItems
    """
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)
    # quantity = models.PositiveIntegerField(default=1)