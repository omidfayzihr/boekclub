from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('profiel/', views.profiel, name='profiel'),
    path('wachtwoord-wijzigen/', views.wachtwoord_wijzigen, name='wachtwoord_wijzigen'),
    path('boek/toevoegen/', views.boek_toevoegen, name='boek_toevoegen'),
    path('boeken/beheer/', views.boeken_beheer, name='boeken_beheer'),
    path('boeken/<int:book_id>/goedkeuren/', views.boek_goedkeuren, name='boek_goedkeuren'),
    path('boeken/<int:book_id>/afkeuren/', views.boek_afkeuren, name='boek_afkeuren'),
    path('leesmoment/toevoegen/', views.leesmoment_toevoegen, name='leesmoment_toevoegen'),
    path('boeken/', views.boeken_overzicht, name='boeken_overzicht'),
    path('newsfeed/', views.Newsfeed, name='newsfeed'),
    path('boeken/<int:book_id>/', views.boek_detail, name='boek_detail'),
    # Ingebouwde auth-urls (login, logout, wachtwoord wijzigen)
    path('', include('django.contrib.auth.urls')),
]
