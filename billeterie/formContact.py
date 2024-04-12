from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    nom = forms.CharField(
        label="Votre nom et prénom", required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrer votre nom et votre prénom'}))
    email = forms.EmailField(
        label="Votre adresse email", required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrer votre adresse email'}))
    sujet = forms.CharField(
        label="Sujet", required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrer le sujet du message'}))
    text = forms.CharField(
        label="Message", required=True,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows':3, 'placeholder': 'Entrer votre message ici'}))

    class Meta:
        model = Contact
        fields = ['nom', 'email', 'sujet', 'text']
