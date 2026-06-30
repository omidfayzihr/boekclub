from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    # 1-op-1 met User: 1 Profile per User. Verwijder je de User, dan ook de Profile.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_genre = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)  # mag leeg zijn

    def __str__(self):
        return self.user.username


# Maak automatisch een bijbehorend Profile zodra er een nieuwe User bijkomt.
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

class Book(models.Model):
    Name = models.CharField(max_length=200)
    PublicationYear = models.IntegerField()
    genre = models.CharField(max_length=100)
    Approved = models.BooleanField(default=False)
    ApprovedBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.Name

class ReadingSession(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Date = models.DateField()
    Score = models.IntegerField(null=True, blank=True)

    class Meta:
        # Een gebruiker mag hetzelfde boek niet meerdere keren op dezelfde dag toevoegen.
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'book', 'Date'],
                name='uniek_leesmoment_per_boek_per_dag',
            )
        ]

    def __str__(self):
        return f"{self.book.Name} ({self.Date})"


