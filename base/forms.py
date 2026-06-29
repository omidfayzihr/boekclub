from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['favorite_genre', 'city', 'date_of_birth']
        labels = {
            'favorite_genre': 'Favoriete genre',
            'city': 'Woonplaats',
            'date_of_birth': 'Geboortedatum',
        }
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }
