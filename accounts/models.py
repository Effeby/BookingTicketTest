from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
  
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    solde = models.IntegerField(default=5000)

    # Add other fields as needed

    def __str__(self):
        return self.user.username
