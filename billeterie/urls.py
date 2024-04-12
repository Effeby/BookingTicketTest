"""
URL configuration for Recrutement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from billeterie import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name="index"),
    path('About/', views.about, name="about"),

    path('Films/', views.movies, name="movies"),
    path('Films-details/<int:film_id>/', views.movies_detail, name="movies_detail"),
    path('Reservation/<int:film_id>/', views.reservation, name="reserver"),

    path('Sport/', views.sport, name="sport"),
    path('Sport-details/', views.sport_detail, name="sport_detail"),
    path('Reservation-nom_sport/', views.reservationSport, name="reserverSport"),

    path('felicitation/', views.felicitation, name="felicitation"),
    path('Telechargement/', views.download, name="appDownload"),
    path('Contact/', views.contact, name='contact'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
