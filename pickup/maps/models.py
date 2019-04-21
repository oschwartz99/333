from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .choices import *

class Event(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, default=-1)
    event_descr = models.CharField(max_length=100, default='')
    event_name  = models.CharField(max_length=50, default='')
    event_type  = models.CharField(max_length=50, choices=EVENT_CHOICES)
    location    = models.CharField(max_length=50, default='')
    public      = models.BooleanField(choices=PUBLIC_CHOICES, blank=False, default=True)
    date        = models.DateField(blank=False, null=True)
    start_time  = models.TimeField(choices=TIME_CHOICES, blank=False, null=True)
    end_time    = models.TimeField(blank=False, null=True)
    lng         = models.FloatField(default=-1)
    lat         = models.FloatField(default=-1)
    users_going = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="upcoming_events")