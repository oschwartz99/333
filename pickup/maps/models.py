from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Event(models.Model):
    user         = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, default=-1)
    event_descr  = models.CharField(max_length = 100, default='descr')
    event_name   = models.CharField(max_length = 50, default='')
    event_type   = models.CharField(max_length=50, default='')
    number_going = models.IntegerField(default=0)
    location     = models.CharField(max_length = 50, default='')

class DebugEvent(models.Model):
    event_descr  = models.CharField(max_length = 100, default='descr')
    event_name   = models.CharField(max_length = 50, default='name')
    event_type   = models.CharField(max_length=50, default='type')
    number_going = models.IntegerField(default=0)
    location     = models.CharField(max_length = 50, default='make a mapbox latev')
