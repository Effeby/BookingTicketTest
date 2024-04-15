from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from billeterie.formContact import ContactForm

from django.core.mail import send_mail
from .models import Reservation_film, film


# Create your views here.

def index(request):
    datas={

    }
    return render(request, 'index.html', datas)


def about(request):
    datas={

    }
    return render(request, 'about.html', datas)


def movies(request):
    films = film.objects.all()
    datas={
        'films': films
    }
    return render(request, 'movie-grid.html', datas)


def movies_detail(request, film_id):
    film_detail = get_object_or_404(film, id=film_id)
    datas = {
        'film_detail': film_detail
    }
    return render(request, 'movie-details.html', datas)

def reservation(request, film_id):
    film_detail = get_object_or_404(film, id=film_id)

    if request.method == 'POST':
        # Récupérer le nombre de tickets souhaité saisi par l'utilisateur
        ticket_quantity = int(request.POST['ticket-quantity'])

        # Calcule le montant total à payer
        total_amount = film_detail.prix * ticket_quantity

        # Vérifie si l'utilisateur a un profil associé
        if hasattr(request.user, 'userprofile'):
            # Vérifie si le solde de l'utilisateur est suffisant
            if request.user.userprofile.solde >= total_amount:
                # Vérifie si les tickets sont disponibles
                if film_detail.place_dispo >= ticket_quantity:
                    # Crée la réservation
                    reservation = Reservation_film.objects.create(
                        user=request.user,
                        movie=film_detail,
                        nb_places_reserves=ticket_quantity
                    )

                    # Déduit le montant du solde de l'utilisateur
                    request.user.userprofile.solde -= total_amount
                    request.user.userprofile.save()

                    # Met à jour le nombre de places disponibles pour le film
                    film_detail.place_dispo -= ticket_quantity
                    film_detail.save()

                    # Envoie un email de confirmation de réservation
                    send_mail(
                        'Confirmation de réservation',
                        'Votre réservation pour le film {} a été confirmée. Nombre de tickets réservés : {}'.format(film_detail.titreFilm, ticket_quantity),
                        settings.EMAIL_HOST_USER,
                        [request.user.email],
                        fail_silently=False,
                    )

                    # Redirige vers la page de confirmation
                    return redirect('felicitation')
                else:
                    # Affiche un message d'erreur
                    error_message = "SOLD OUT. Désolé, il n'y a pas suffisamment de places disponibles."
            else:
                # Affiche un message d'erreur
                error_message = "Votre solde est insuffisant. Veuillez recharger votre compte."
        else:
            # Gérer le cas où l'utilisateur n'a pas de profil associé
            error_message = "Votre compte n'a pas de profil associé. Veuillez contacter l'administrateur."

        # Renvoie la même page avec le message d'erreur
        datas = {
            'film_detail': film_detail,
            'error_message': error_message,
            'ticket_quantity': ticket_quantity  # Rétablir le nombre de tickets saisi par l'utilisateur
        }
        return render(request, 'movie-checkout.html', datas)
    else:
        # Si la méthode HTTP n'est pas POST, renvoie simplement l'utilisateur à la page de réservation
        return render(request, 'movie-checkout.html', {'film_detail': film_detail})



def sport(request):
    datas={

    }
    return render(request, 'sports.html', datas)

def sport_detail(request):
    datas={

    }
    return render(request, 'sport-details.html', datas)

def reservationSport(request):
    datas={

    }
    return render(request, 'sports-checkout.html', datas)

def felicitation(request):
    datas={

    }
    return render(request, 'felicitation.html', datas)


def download(request):
    datas={

    }
    return render(request, 'apps-download.html', datas)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            print("Votre Message a bien été envoyé")
            return redirect('contact')
    else:
        form = ContactForm()

    datas = {
        'form': form,
    }

    return render(request, 'contact.html', datas)