from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.template.context_processors import csrf
from .forms import CreateEvent
from .models import Event, DebugEvent
import django
from django.middleware.csrf import get_token
from django.http import JsonResponse


def default_map(request):
    return render(request, 'default.html', {'mapbox_access_token': 'pk.eyJ1IjoiY29zMzMzIiwiYSI6ImNqdDYzY3A0ZDBkMGc0YXF4azczdXRheWMifQ.3VeYeV_c-231Lab62H2XtQ'})

def testing_list_events(request):
    all_debug_events = DebugEvent.objects.all()
    all_events = Event.objects.all()
    return render(request, 'testing.html', {'all_events': all_events, 'all_debug_events': all_debug_events})

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
            new_event = Event(event_name=event_name, event_descr=event_descri, number_going=number_going, location=location, user=user)
            new_event.save()
            return render(request, 'testing.html', {'csrf_token': csrf_token})
    return render(request, 'testing.html', {'event_form': event_form})

def testing_map_def(request):
    return render(request, "map_def.html")

def fetch_from_db(request):
    all_events = Event.objects.all()
    print(type(all_events))
    data = {
        'events':{}
    }
    for event in all_events:
        data['events'][event.event_name] = event.event_descr
    return JsonResponse(data)
