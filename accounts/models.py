from django.db import models
from django.contrib.auth.models import User
from .constants import GENDER_TYPE

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name= 'profile')
    profile_picture = models.ImageField(upload_to='accounts/profile_pictures/', null=True, blank=True)
    birth_date = models.DateField(null= True, blank= True)
    gender = models.CharField(max_length= 10, choices= GENDER_TYPE)
    street_address = models.CharField(max_length= 100)
    city = models.CharField(max_length= 100)
    postal_code = models.PositiveIntegerField()
    balance = models.DecimalField(default= 0, max_digits= 12, decimal_places=2)
    membership_creation_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.id} {self.user.username}"
    

    