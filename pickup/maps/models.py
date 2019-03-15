from django.db import models

class Event(models.Model):
    event_name   = models.CharField(max_length = 50)
    event_type   = models.CharField(max_length=50)
    number_going = models.IntegerField()
    location     = models.CharField(max_length = 50)
    icon         = models.CharField(max_length = 50)

