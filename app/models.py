
from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser


class Usercustome(AbstractUser):
    ROLE_CHOICES = (
        ('shopkeeper', 'shopkeeper'),
        ('customer', 'customer'),
    )

    phone_number = models.CharField(max_length=15,null=True, blank=True)
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES
    )

    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return f"{self.username} - {self.role}"



# creaet user profile 
class UserProfile(models.Model):
    user = models.OneToOneField(Usercustome, on_delete=models.CASCADE)
    address = models.TextField(max_length=1000)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    shop_name = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f"Profile of {self.user.username}"
    
# class LocationShop(models.Model):
#     shop = models.OneToOneField(Usercustome, on_delete=models.CASCADE)
#     latitude = models.DecimalField(max_digits=9, decimal_places=6)
#     longitude = models.DecimalField(max_digits=9, decimal_places=6)
#     address = models.TextField(blank=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"Location of {self.shop.username}"

#     def google_maps_url(self):
#         return f"https://www.google.com/maps?q={self.latitude},{self.longitude}"