
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
    ('00:00:00', 'Midnight'),
    ('01:00:00', '1 AM'),
    ('02:00:00', '2 AM'),
    ('03:00:00', '3 AM'),
    ('04:00:00', '4 AM'),
    ('05:00:00', '5 AM'),
    ('06:00:00', '6 AM'),
    ('07:00:00', '7 AM'),
    ('08:00:00', '8 AM'),
    ('09:00:00', '9 AM'),
    ('10:00:00', '10 AM'),
    ('11:00:00', '11 AM'),
    ('12:00:00', 'Noon'),
    ('13:00:00', '1 PM'),
    ('14:00:00', '2 PM'),
    ('15:00:00', '3 PM'),
    ('16:00:00', '4 PM'),
    ('17:00:00', '5 PM'),
    ('18:00:00', '6 PM'),
    ('19:00:00', '7 PM'),
    ('20:00:00', '8 PM'),
    ('21:00:00', '9 PM'),
    ('22:00:00', '10 PM'),
    ('23:00:00', '11 PM'), 
)
