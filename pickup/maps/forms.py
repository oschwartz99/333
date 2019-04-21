from django import forms
from .choices import *
from bootstrap_datepicker_plus import DatePickerInput
from emoji_picker.widgets import EmojiPickerTextInput, EmojiPickerTextarea
from .models import *

class CreateEvent(forms.Form):
    event_name   = forms.CharField(label="Give your event a name.", max_length = 50)
    event_descr  = forms.CharField(label="Say something about your event.", max_length=100)
    event_type   = forms.ChoiceField(label="What type of event do you want to create?", choices=EVENT_CHOICES, required=True)
    location     = forms.CharField(label="Where is your event occuring?", max_length = 50)
    public       = forms.ChoiceField(choices=PUBLIC_CHOICES, label="Do you want your event to be public?", widget=forms.Select(), required=True)
    date         = forms.DateTimeField(label="What date will your event occur?")
    start_time   = forms.ChoiceField(choices=TIME_CHOICES, label="When will your event start?")
    end_time     = forms.ChoiceField(choices=TIME_CHOICES, label="When will your event end?")
    lng          = forms.FloatField()
    lat          = forms.FloatField()