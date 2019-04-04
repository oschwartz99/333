from django import forms
from maps.icons import *
from bootstrap_datepicker_plus import DatePickerInput
from .models import *

class CreateEvent(forms.Form):
    event_name   = forms.CharField(label="Give your event a name.", max_length = 50)
    event_descr  = forms.CharField(label="Say something about your event.", max_length=100)
    event_type   = forms.ChoiceField(label="What type of event do you want to create?", choices=EVENT_CHOICES, required=True)
    datetime     = forms.DateTimeField(validators=[validate_datetime], label="When will your event occur?")
    location     = forms.CharField(label="Where is your event occuring?", max_length = 50)
    lng          = forms.FloatField()
    lat          = forms.FloatField()

