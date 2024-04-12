from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class film(models.Model):
    titreFilm = models.CharField(max_length = 300)
    imageFilm = models.ImageField(upload_to='AfficheFilm/', blank=True, null=True)
    resume = models.TextField(max_length=2000, blank=True)
    lieu_cinema = models.CharField(max_length=300, blank=True,)
    nom_realisateur = models.CharField(max_length=300)
    image_realisateur = models.ImageField(upload_to='imgRealisateur/', blank=True, null=True)
    bande_annonce = models.CharField(max_length=500, blank=True, null=True)
    langue = models.TextField(max_length=300)
    categorie = models.TextField(max_length=300)
    debut_seance = models.TimeField(blank=True, null=True)
    date_sortie = models.DateField(blank=True, null=True)
    dure_film = models.TimeField(blank=True, null=True)
    list_acteur = models.CharField(max_length=700)
    equipage = models.CharField(max_length=700)
    place_dispo = models.IntegerField(default=0)
    prix = models.IntegerField(default=0)

    #standards
    status = models.BooleanField(default= True)
    date_add = models.DateTimeField(auto_now = True)
    date_update =models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.titreFilm} - {self.nom_realisateur} - ({self.date_sortie})"



class Reservation_film(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # Ajout du champ user
    movie = models.ForeignKey(film, on_delete=models.CASCADE, null=True, blank=True)  # Relation avec le film
    nb_places_reserves = models.IntegerField(default=0)
    date_reservation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Reservation {self.id} - {self.user.username} - {self.movie.titreFilm}'

    #standards
    status = models.BooleanField(default= True)
    date_add = models.DateTimeField(auto_now = True)
    date_update =models.DateTimeField(auto_now = True)
    
    def __str__(self):
        if self.movie:
            return f"Reservation pour {self.movie.titreFilm}"
        else:
            return "Reservation non liée à un film"
        

class Contact(models.Model):
    nom= models.CharField(max_length= 250)
    email= models.EmailField()
    sujet= models.TextField()
    text= models.TextField()

    #standards
    status = models.BooleanField(default= True)
    date_add = models.DateTimeField(auto_now = True)
    date_update =models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.nom