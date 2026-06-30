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
    path('boeken/<int:book_id>/leesmoment/', views.leesmoment_toevoegen, name='leesmoment_voor_boek'),
    path('mijn-leesmomenten/', views.mijn_leesmomenten, name='mijn_leesmomenten'),
    path('leesmoment/<int:pk>/aanpassen/', views.leesmoment_aanpassen, name='leesmoment_aanpassen'),
    path('leesmoment/<int:pk>/verwijderen/', views.leesmoment_verwijderen, name='leesmoment_verwijderen'),
    path('leesmomenten/beheer/', views.leesmomenten_beheer, name='leesmomenten_beheer'),
    path('leesmomenten/<int:pk>/verwijderen/', views.leesmoment_admin_verwijderen, name='leesmoment_admin_verwijderen'),
    path('boeken/', views.boeken_overzicht, name='boeken_overzicht'),
    path('newsfeed/', views.newsfeed, name='newsfeed'),
    path('boeken/<int:book_id>/', views.boek_detail, name='boek_detail'),
    path('gebruiker/<str:username>/', views.publiek_profiel, name='publiek_profiel'),
    # Ingebouwde auth-urls (login, logout, wachtwoord wijzigen)
    path('', include('django.contrib.auth.urls')),
]
