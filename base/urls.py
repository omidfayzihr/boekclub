from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    # Ingebouwde auth-urls (login, logout, wachtwoord wijzigen, ...)
    path('', include('django.contrib.auth.urls')),
]
