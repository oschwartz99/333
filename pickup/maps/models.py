from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Event(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.PROTECT, default=-1)
    event_descr = models.CharField(max_length=100, default='descr')
    event_name = models.CharField(max_length=50, default='')
    event_type = models.CharField(max_length=50, default='')
    number_going = models.IntegerField(default=0)
    location = models.CharField(max_length=50, default='')


class DebugEvent(models.Model):
    user = models.CharField(max_length=50, default='-1')
    event_descr = models.CharField(max_length=100, default='-1')
    event_name = models.CharField(max_length=50, default='-1')
    event_type = models.CharField(max_length=50, default='-1')
    number_going = models.IntegerField(default=0)
    location = models.CharField(max_length=50, default='-1')

    def __str__(self):
        return self.event_name + ": " + self.event_descr
