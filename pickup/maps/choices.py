
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

TIME_CHOICES = (
	('06:00:00', '6 am'),
    ('07:00:00', '7 am'),
    ('00:00:00', '8 am'), 
)
