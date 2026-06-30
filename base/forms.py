from django import forms
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
        widgets = {
            'Date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['book'].queryset = Book.objects.filter(Approved=True)