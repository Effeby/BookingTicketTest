from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login as auth_login
from django.urls import reverse  # Fix the import statement
from .models import UserProfile

from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


# déconnexion
def logout_view(request):
    logout(request)
    return redirect('/')



def register(request):
    if request.method == 'POST':
        # Retrieve form data
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Check if the username or email already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'sign-up.html', {'error_message': 'Ce username existe déja, veuillez en choisir un autre .'})
        if User.objects.filter(email=email).exists():
            return render(request, 'sign-up.html', {'error_message': 'Cet email existe déja, veuillez en choisir un autre .'})

        try:
            # Create a new user
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            # Create Profile

            # Create UserProfile
            user_profile = UserProfile.objects.create(user=user, email=email,)

            # Log in the user
            authenticated_user = authenticate(request, username=username, password=password)
            auth_login(request, authenticated_user)

            # Add a success message
            messages.success(request, 'Registration successful. You are now logged in.')

            # Redirect to a success page or any other page
            return redirect('login')

        except Exception as e:
            return render(request, 'sign-up.html', {'error_message': str(e)})

    # If not a POST request, render the registration form
    return render(request, 'sign-up.html')



def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Authenticate the user using UserProfile
        user_profile = UserProfile.objects.filter(email=email).first()
        if user_profile:
            user = authenticate(request, username=user_profile.user.username, password=password)
            if user is not None:
                # Authenticated successfully
                auth_login(request, user)
                # Redirect to a success page
                return redirect('index')
            else:
                # Authentication failed
                return render(request, 'sign-in.html', {'error_message': 'Email ou mot de passe invalide. Veuillez réessayer.'})
        else:
            # User with given email not found
            return render(request, 'sign-in.html', {'error_message': 'Email ou mot de passe invalide. Veuillez réessayer.'})

    # If not a POST request, render the login form
    return render(request, 'sign-in.html')



def blog(request):
    
    datas = {
        
       
    }

    return render(request, "blog.html", datas)


def Parametre(request):

    datas = {
        
       
    }

    return render(request, "Parametre.html", datas)



def reset(request, email=None):
    if request.method == 'POST':
        email = request.POST.get('email', email)  # Utilisez l'e-mail fourni dans le formulaire, s'il existe
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Vérifier si les mots de passe correspondent
        if password != confirm_password:
            # Gérer l'erreur de non-correspondance des mots de passe
            return render(request, "reset_password.html", {'email': email, 'error_message': "Les mots de passe ne correspondent pas."})

        # Vérifier si l'utilisateur existe avec l'adresse e-mail fournie
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            # Gérer l'erreur si l'utilisateur n'existe pas
            return render(request, "reset_password.html", {'email': email, 'error_message': "Aucun utilisateur n'existe avec cette adresse e-mail."})

        # Changer le mot de passe de l'utilisateur
        user.set_password(password)
        user.save()

        # Rediriger vers une page de confirmation ou de connexion
        return redirect('login')  # Rediriger vers la page de connexion après avoir réinitialisé le mot de passe

    # Si ce n'est pas une requête POST, simplement rendre la page avec le formulaire
    return render(request, "reset_password.html", {'email': email})

def sendmail(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        # Vérifiez si l'e-mail existe dans la base de données
        if User.objects.filter(email=email).exists():
            # L'utilisateur existe dans la base de données, vous pouvez envoyer l'e-mail de réinitialisation
            reset_link = request.build_absolute_uri(reverse('reset_with_email', kwargs={'email': email}))  # Obtenez l'URL vers la vue reset_password

            # Envoyez l'e-mail avec le lien de réinitialisation
            send_mail(
                'Réinitialisation de mot de passe',
                f'Cliquez sur ce lien pour réinitialiser votre mot de passe : {reset_link}',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )

            return render(request, 'reset_email_sent.html')  # Renvoyer la page HTML pour indiquer que l'e-mail a été envoyé avec succès
        else:
            # L'utilisateur n'existe pas dans la base de données
            error_message = "L'adresse e-mail fournie n'existe pas dans notre base de données."
            return render(request, 'sendmailReset.html', {'error_message': error_message})

    return render(request, 'sendmailReset.html')

