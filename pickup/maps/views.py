from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.template.context_processors import csrf

from .forms import CreateEvent
from .models import Event, DebugEvent
import django
from django.middleware.csrf import get_token


def default_map(request):
    return render(request, 'default.html', {'mapbox_access_token': 'pk.eyJ1IjoiY29zMzMzIiwiYSI6ImNqdDYzY3A0ZDBkMGc0YXF4azczdXRheWMifQ.3VeYeV_c-231Lab62H2XtQ'})

def testing_list_events(request):
    all_events = DebugEvent.objects.all()
    return render_to_response('testing.html', {'all_events': all_events})

def testing_view(request):
    if request.method == 'GET':
        event_form = CreateEvent()
    elif request.method == 'POST':
        event_form = CreateEvent(request.POST)
        if event_form.is_valid():
            csrf_token   = get_token(request)
            print(csrf_token)
            event_descri = event_form.cleaned_data['event_descr']
            event_name   = event_form.cleaned_data['event_name']
            event_type   = event_form.cleaned_data['event_type']
            number_going = event_form.cleaned_data['number_going']
            location     = event_form.cleaned_data['location']
            user         = request.user
            new_event = Event(event_name=event_name, event_descri=event_descri, number_going=number_going, location=location, icon=icon, user=user)
            new_event.save()
            return render_to_response('testing.html', {'csrf_token': csrf_token})
    return render_to_response('testing.html', {'event_form': event_form})
    
