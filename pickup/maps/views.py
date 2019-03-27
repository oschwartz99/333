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
            event_descr = event_form.cleaned_data['event_descr']
            event_name   = event_form.cleaned_data['event_name']
            event_type   = event_form.cleaned_data['event_type']
            number_going = event_form.cleaned_data['number_going']
            location     = event_form.cleaned_data['location']
            lat          = event_form.cleaned_data['lat']
            lng          = event_form.cleaned_data['lng']
            user         = request.user
            new_event = Event(event_name=event_name, event_type=event_type, event_descr=event_descr, number_going=number_going, location=location, lat=lat, lng=lng, user=user)
            new_event.save()
            return render(request, 'testing.html', {'csrf_token': csrf_token})
    return render(request, 'testing.html', {'event_form': event_form})

def testing_map_def(request):
    return render(request, "map_def.html")

# Return all events from the database as a JSON object
def fetch_from_db(request):
    all_events = Event.objects.all()
    data = {
        'events':{}
    }
    for event in all_events:
        dict = {
            'created_by': event.user.username,
            'event_descr': event.event_descr,
            'event_type': event.event_type,
            'number_going': event.number_going,
            'location': event.location,
            'lng': event.lng,
            'lat': event.lat,
        }
        data['events'][event.event_name] = dict
    return JsonResponse(data)
