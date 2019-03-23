from django import forms

EVENT_CHOICES = (
    ("Party", "Party"),
    ("Concert", "Concert"),
)

class CreateEvent(forms.Form):
    event_descr  = forms.CharField(max_length=100)
    event_name   = forms.CharField(max_length = 50)
    event_type   = forms.ChoiceField(choices=EVENT_CHOICES, required=True)
    number_going = forms.IntegerField()
    location     = forms.CharField(max_length = 50)
    lng          = forms.FloatField()
    lat          = forms.FloatField()

