from django.contrib import admin
from .models import (film, Reservation_film, Contact)

# Register your models here.
admin.site.register(film)
admin.site.register(Reservation_film)
admin.site.register(Contact)