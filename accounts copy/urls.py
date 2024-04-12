
from django.urls import path
from accounts import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path("Profil", views.Profil, name="Profil"),
    path("Parametre", views.Parametre, name="Parametre"),
    path("Edit_Profil", views.Edit_Profil, name="Edit_Profil"),
    path('change_profile_picture', views.change_profile_picture, name='change_profile_picture'),
    path('blog/', views.blog, name='blog'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('tables/', views.tables, name='tables'),
    path('reset_link/', views.sendmail, name='resetlink'),
    path('reset_password/<str:email>/', views.reset, name='reset_with_email'),  # Nouvelle URL pour la réinitialisation avec l'e-mail
    path('reset_password/', views.reset, name='reset'),  # Assurez-vous que la vue est nommée 'reset'

    
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
