
### File for describing the different event types available
### Utilized in models.py, forms.py, and load.js

EVENT_CHOICES = (
    ("Party", "Party"),
    ("Concert", "Concert"),
    ("Study", "Study"),
    ("Speech", "Speech"),
    ("Meal", "Meal"),
    ("Movie", "Movie"),
    ("Sports", "Sports"),
)

PUBLIC_CHOICES = (
    (True, 'Public - visible to everyone'),
    (False, 'Private - visible to your friends'),
)
