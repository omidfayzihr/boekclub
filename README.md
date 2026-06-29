# boekclub
Eindopdracht: Boekclub Leeslogboek

## Installeren en starten
1. Installeer de benodigde pakketten:
   ```
   pip install -r requirements.txt
   ```
2. Voer de migraties uit:
   ```
   python manage.py migrate
   ```
3. Maak een admin-account aan (gebruikersnaam en wachtwoord: `admin`):
   ```
   python manage.py createsuperuser
   ```
4. Start de server:
   ```
   python manage.py runserver
   ```
