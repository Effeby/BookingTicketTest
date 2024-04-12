from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics', default='default_profile.png')
    phone_number = models.CharField(max_length=20, blank=True, null=True)  # Ajout du numéro de téléphone
    bio = models.TextField(blank=True, null=True)  # Ajout de la bio
    facebook = models.URLField(max_length=200, blank=True, null=True)  # Ajout du lien vers Facebook
    twitter = models.URLField(max_length=200, blank=True, null=True)  # Ajout du lien vers Twitter
    instagram = models.URLField(max_length=200, blank=True, null=True)  # Ajout du lien vers Instagram
    linkedin = models.URLField(max_length=200, blank=True, null=True)  # Ajout du lien vers LinkedIn
    

    def __str__(self):
        return f'{self.user.username} Profile'

class UserProfile(models.Model):
    PROFILE_CHOICES = [
        ('recruteur', 'Recruteur'),
        ('postulant', 'Postulant'),
        # Add other choices as needed
    ]
  
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    profile = models.CharField(max_length=255, choices=PROFILE_CHOICES)
    entreprise = models.CharField(max_length=255)
    # Add other fields as needed

    def __str__(self):
        return self.user.username
