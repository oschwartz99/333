from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .choices import *

def validate_datetime(dt):
    if dt < timezone.now():
        raise ValidationError(
            ('Date must be in the future! Please refresh the page.')
        )

class Event(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.PROTECT, default=-1)
    event_descr = models.CharField(max_length=100, default='')
    event_name = models.CharField(max_length=50, default='')
    event_type = models.CharField(max_length=50, choices=EVENT_CHOICES)
    public = models.BooleanField(choices=PUBLIC_CHOICES, blank=False, default=True)
    datetime = models.DateTimeField(blank=False, null=True, validators=[validate_datetime])
    duration = models.TimeField(blank=False, null=True)
    location = models.CharField(max_length=50, default='')
    lng = models.FloatField(default=-1)
    lat = models.FloatField(default=-1)
    users_going = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="upcoming_events")