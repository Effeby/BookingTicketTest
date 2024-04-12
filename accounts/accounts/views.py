from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login as auth_login
from django.urls import reverse  # Fix the import statement
from .models import UserProfile
from .models import Profile
from .forms import ProfileForm
from AppRecrutement.models import Emplois 
from AppRecrutement.models import Candidature 
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
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        profile_type = request.POST['profile']
        password = request.POST['password']
        entreprise = request.POST['entreprise']

        # Check if the username or email already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error_message': 'Ce username existe déja, veuillez en choisir un autre .'})
        if User.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error_message': 'Cet email existe déja, veuillez en choisir un autre .'})

        try:
            # Create a new user
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            # Create Profile
            profile = Profile.objects.create(user=user, image='profile_pics/default_profile.png')

            # Create UserProfile
            user_profile = UserProfile.objects.create(user=user, first_name=first_name, last_name=last_name, email=email, profile=profile_type, entreprise=entreprise)

            # Log in the user
            authenticated_user = authenticate(request, username=username, password=password)
            auth_login(request, authenticated_user)

            # Add a success message
            messages.success(request, 'Registration successful. You are now logged in.')

            # Redirect to a success page or any other page
            return redirect('login')

        except Exception as e:
            return render(request, 'register.html', {'error_message': str(e)})

    # If not a POST request, render the registration form
    return render(request, 'register.html')



def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            # Add a success message
            messages.success(request, 'Login successful.')
            # Redirect to a success page, you can customize this based on your app
            return redirect('index')
        else:
            # Add an error message
            return render(request, 'login.html', {'error_message': 'Username ou mot de passe invalide. Veuillez réessayer.'})

    # If not a POST request, render the login form
    return render(request, 'login.html')



def Profil(request):
    user = request.user
    return render(request, 'Profil.html', {'user': user})


def change_profile_picture(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('Profil')  # Redirigez l'utilisateur vers la page de profil après avoir modifié la photo de profil
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'change_profile_picture.html', {'form': form})


def Edit_Profil(request):
    user = request.user
    profile = Profile.objects.get_or_create(user=user)[0]  # Récupérer le profil ou créer s'il n'existe pas

    if request.method == 'POST':
        # Mettre à jour les données de l'utilisateur
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.username = request.POST.get('username', user.username)
        user.email = request.POST.get('email', user.email)
        user.save()

        # Mettre à jour les données du profil
        profile.phone_number = request.POST.get('phone_number', profile.phone_number)
        profile.bio = request.POST.get('bio', profile.bio)
        profile.facebook = request.POST.get('facebook', profile.facebook)
        profile.twitter = request.POST.get('twitter', profile.twitter)
        profile.instagram = request.POST.get('instagram', profile.instagram)
        profile.linkedin = request.POST.get('linkedin', profile.linkedin)
        profile.save()

        messages.success(request, 'Profil mis à jour avec succès.')
        return redirect('Profil')  # Rediriger vers la page de profil

    else:
        context = {
            'profile': profile  # Passer le profil à utiliser dans le template
        }
        return render(request, 'Edit_Profil.html', context)
    

def dashboard(request):
    # Récupérer les emplois créés par l'utilisateur connecté
    emplois_utilisateur = Emplois.objects.filter(user=request.user)
    
    mes_emplois = Emplois.objects.filter(user=request.user).order_by('-date_add')[:3]

    # Compter le nombre total de candidatures associées à tous les emplois de l'utilisateur connecté, mais uniquement les candidatures reçues par cet utilisateur
    total_candidatures = Candidature.objects.filter(nom_poste__in=mes_emplois).count()
    
    # Récupérer les candidatures associées à ces emplois de l'utilisateur connecté
    candidatures = Candidature.objects.filter(nom_poste__in=emplois_utilisateur)


    # Autres données à afficher sur le tableau de bord (par exemple, des statistiques)
    total_emplois = Emplois.objects.filter(user=request.user).count()

    datas = {
        'mes_emplois': mes_emplois,
        'total_candidatures': total_candidatures,
        'total_emplois': total_emplois,
        'candidatures': candidatures
        
    }

    return render(request, "dashboard.html", datas)


def blog(request):
    
    datas = {
        
       
    }

    return render(request, "blog.html", datas)


def Parametre(request):

    datas = {
        
       
    }

    return render(request, "Parametre.html", datas)


def tables(request):
    # Récupérer les emplois créés par l'utilisateur connecté
    emplois_utilisateur = Emplois.objects.filter(user=request.user)
    
    mes_emplois = Emplois.objects.filter(user=request.user).order_by('-date_add')[:3]

    # Compter le nombre total de candidatures associées à tous les emplois de l'utilisateur connecté, mais uniquement les candidatures reçues par cet utilisateur
    total_candidatures = Candidature.objects.filter(nom_poste__in=mes_emplois).count()
    
    # Récupérer les candidatures associées à ces emplois de l'utilisateur connecté
    candidatures = Candidature.objects.filter(nom_poste__in=emplois_utilisateur)
    
    datas = {
        'mes_emplois': mes_emplois,
        'total_candidatures': total_candidatures,
        'candidatures': candidatures
    }
    
    return render(request, 'tables.html', datas)



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

