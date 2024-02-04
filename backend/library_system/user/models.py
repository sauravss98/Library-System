from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    STATUS = (
        ("admin","admin"),
        ("student","student")
    )

    email = models.EmailField(unique = True)
    status = models.CharField(max_length = 100, choices = STATUS,default="student")
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
    