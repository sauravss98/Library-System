from django.db import models

# Create your models here.
class Book(models.Model):
    book_id = models.IntegerField()
    title = models.CharField(max_length=255)
    authorName = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title

    # @property
    # def is_available(self):
    #         return False
    #     else:
    #         return True