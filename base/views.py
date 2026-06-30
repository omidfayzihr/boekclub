from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import BookForm, ProfileForm, ReadingSessionForm
from .models import Book, ReadingSession
from django.core.paginator import Paginator
from django.db.models import Avg, Count



def index(request):
    return render(request, 'base/index.html')


def register(request):
    # Bij POST het formulier valideren en opslaan, daarna direct inloggen.
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account aangemaakt, je bent ingelogd.')
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def profiel(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profiel bijgewerkt.')
            return redirect('profiel')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'base/profiel.html', {'form': form, 'profile': profile})


@login_required
def wachtwoord_wijzigen(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # blijf ingelogd
            messages.success(request, 'Wachtwoord gewijzigd.')
            return redirect('profiel')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'base/wachtwoord_wijzigen.html', {'form': form})


@login_required
def boek_toevoegen(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            if request.user.is_staff:
                book.Approved = True
                book.ApprovedBy = request.user
                messages.success(request, 'Boek toegevoegd en direct goedgekeurd.')
            else:
                book.Approved = False
                messages.success(request, 'Boek toegevoegd en wacht op goedkeuring.')
            book.save()
            return redirect('index')
    else:
        form = BookForm()
    return render(request, 'base/boek_toevoegen.html', {'form': form})


def is_admin(user):
    return user.is_staff

@login_required
@user_passes_test(is_admin)
def boeken_beheer(request):
    boeken = Book.objects.filter(Approved=False)
    return render(request, 'base/boeken_beheer.html', {'boeken': boeken})


@login_required
@user_passes_test(is_admin)
def boek_goedkeuren(request, book_id):
    book = Book.objects.get(id=book_id)
    book.Approved = True
    book.ApprovedBy = request.user
    book.save()
    messages.success(request, f'"{book.Name}" goedgekeurd.')
    return redirect('boeken_beheer')


@login_required
@user_passes_test(is_admin)
def boek_afkeuren(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    messages.success(request, f'"{book.Name}" afgekeurd en verwijderd.')
    return redirect('boeken_beheer')

@login_required
def leesmoment_toevoegen(request):
    if request.method == 'POST':
        form = ReadingSessionForm(request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            session.user = request.user
            session.save()
            messages.success(request, 'Leesmoment toegevoegd.')
            return redirect('index')
    else:
        form = ReadingSessionForm()
    return render(request, 'base/leesmoment_toevoegen.html', {'form': form})

def boeken_overzicht(request):
    boeken_list = Book.objects.filter(Approved=True).order_by('Name')
    paginator = Paginator(boeken_list, 20)  # 20 boeken per pagina
    page_number = request.GET.get('page')
    boeken = paginator.get_page(page_number)
    return render(request, 'base/boeken_overzicht.html', {'boeken': boeken})

def Newsfeed(request):
    sessies = ReadingSession.objects.all().order_by('-Date')
    return render(request, 'base/newsfeed.html', {'sessies': sessies})

def boek_detail(request, book_id):
    boek = get_object_or_404(Book, id=book_id)
    return render(request, 'base/boek_detail.html', {'boek': boek})

def boek_detail(request, book_id):
    # Haal het boek op
    boek = get_object_or_404(Book, id=book_id)
    gemiddelde = boek.readingsession_set.aggregate(Avg('Score'))['Score__avg']
    
    if gemiddelde is not None:
        gemiddelde = round(gemiddelde, 1)
        
    context = {
        'boek': boek,
        'gemiddelde_score': gemiddelde
    }
    return render(request, 'base/boek_detail.html', context)