from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Book, ReadingSession



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

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['Name', 'PublicationYear', 'genre']
    

class ReadingSessionForm(forms.ModelForm):
    class Meta:
        model = ReadingSession
        fields = ['book', 'Date', 'Score']
        labels = {
            'book': 'Boek',
            'Date': 'Datum',
            'Score': 'Score',
        }
        widgets = {
            'Date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        # Je kunt alleen goedgekeurde boeken kiezen.
        self.fields['book'].queryset = Book.objects.filter(Approved=True)

    def clean(self):
        cleaned = super().clean()
        boek = cleaned.get('book')
        datum = cleaned.get('Date')
        # Niet twee keer hetzelfde boek op dezelfde dag voor dezelfde gebruiker.
        if self.user and boek and datum:
            bestaand = ReadingSession.objects.filter(user=self.user, book=boek, Date=datum)
            if self.instance.pk:
                bestaand = bestaand.exclude(pk=self.instance.pk)
            if bestaand.exists():
                raise forms.ValidationError('Je hebt dit boek op deze dag al toegevoegd.')
        return cleaned


class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Geen lange helpteksten onder de velden tonen.
        for veld in self.fields.values():
            veld.help_text = ''