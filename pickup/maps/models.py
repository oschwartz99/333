from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Event(models.Model):
    user         = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    event_descr  = models.CharField(max_length = 100)
    event_name   = models.CharField(max_length = 50)
    event_type   = models.CharField(max_length=50)
    number_going = models.IntegerField()
    location     = models.CharField(max_length = 50)
    icon         = models.CharField(max_length = 50)

