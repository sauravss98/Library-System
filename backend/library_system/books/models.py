from django.db import models

# Create your models here.
class Book(models.Model):
    """
    Model Class for Book
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title

    @property
    def is_available(self):
        """
        Function to return if book is available or not
        """
        if self.quantity ==0:
            return False
        else:
            return True
