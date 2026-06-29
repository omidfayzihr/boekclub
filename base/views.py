from django.shortcuts import render, redirect
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProfileForm


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
