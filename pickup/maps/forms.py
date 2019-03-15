from django import forms

class CreateEvent(forms.Form):
    event_descr  = forms.CharField(max_length=100)
    event_name   = forms.CharField(max_length = 50)
    event_type   = forms.CharField(max_length=50)
    number_going = forms.IntegerField()
    location     = forms.CharField(max_length = 50)