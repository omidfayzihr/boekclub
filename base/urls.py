from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('profiel/', views.profiel, name='profiel'),
    path('wachtwoord-wijzigen/', views.wachtwoord_wijzigen, name='wachtwoord_wijzigen'),
    # Ingebouwde auth-urls (login, logout, wachtwoord wijzigen)
    path('', include('django.contrib.auth.urls')),
]
