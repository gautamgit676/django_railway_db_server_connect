
from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser


class Usercustome(AbstractUser):
    ROLE_CHOICES = (
        ('shopkeeper', 'Shopkeeper'),
        ('customer', 'Customer'),
    )

    phone_number = models.CharField(max_length=15,null=True, blank=True)
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES
    )

    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return f"{self.username} - {self.role}"
