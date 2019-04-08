import django
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.template.context_processors import csrf
from django.middleware.csrf import get_token
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from bootstrap_datepicker_plus import DateTimePickerInput
from .forms import CreateEvent
from .models import Event

def ajax_add_event(request):
    event_form = CreateEvent()
    event_form.fields['datetime'].widget = DateTimePickerInput()
    rendered = render_to_string('add-event.html', {'event_form': event_form}, request=request)
    data = {
        'page': rendered,
    }
    return JsonResponse(data)

def ajax_add_event(request):
    event_form = CreateEvent()
    event_form.fields['datetime'].widget = DateTimePickerInput()
    rendered = render_to_string('add-event.html', {'event_form': event_form}, request=request)
    data = {
        'page': rendered,
    }
    return JsonResponse(data)

def ajax_home_sb(request):
    rendered = render_to_string('home_sb.html', request=request)
    data = {
        'page': rendered,
    }
    return JsonResponse(data)

def ajax_profile_sb(request):
    rendered = render_to_string('profile/profile_sb.html', request=request)
    if request.GET.get("which") == "edit":
        form = CustomUserChangeForm(instance=request.user)
        rendered = render_to_string('profile/profile_edit.html', {'form': form} ,request=request)
    data = {
        'page': rendered,
    }
    return JsonResponse(data)

def default_map(request):
    # An event was added
    if request.method == 'POST':
        event_form = CreateEvent(request.POST)
        if event_form.is_valid():
            csrf_token   = get_token(request)
            event_descr = event_form.cleaned_data['event_descr']
            event_name   = event_form.cleaned_data['event_name']
            event_type   = event_form.cleaned_data['event_type']
            datetime    = event_form.cleaned_data['datetime']
            location     = event_form.cleaned_data['location']
            lat          = event_form.cleaned_data['lat']
            lng          = event_form.cleaned_data['lng']
            user         = request.user
            new_event = Event(event_name=event_name, event_type=event_type, datetime=datetime, event_descr=event_descr, location=location, lat=lat, lng=lng, user=user)
            new_event.save()
            new_event.users_going.add(user)

            # Send user to home page
            return render(request, 'main.html', {'csrf_token': csrf_token})
    elif request.method == 'GET':
        return render(request, 'main.html', {'mapbox_access_token': 'pk.eyJ1IjoiY29zMzMzIiwiYSI6ImNqdDYzY3A0ZDBkMGc0YXF4azczdXRheWMifQ.3VeYeV_c-231Lab62H2XtQ'})

# Return all events from the database as a JSON object
def fetch_from_db(request):
    all_events = Event.objects.all()
    data = {
        'events':{}
    }
    for event in all_events:
        # Set a boolean value is the logged-in user 
        # is going to a given event
        going = False
        for user_going in event.users_going.all():
            if user_going.id == request.user.id:
                going = True
        number_going = event.users_going.count()
        
        dict = {
            'number_going': number_going,
            'user_going': going,
            'event_id':event.id,
            'created_by': event.user == request.user, # if user created given event
            'event_descr': event.event_descr,
            'event_type': event.event_type,
            'location': event.location,
            'lng': event.lng,
            'lat': event.lat,
        }
        data['events'][event.event_name] = dict
    return JsonResponse(data)

# Update the given event to show the user is going
def user_going(request):
    event_list = list(Event.objects.filter(id=request.GET.get("event_id")))
    if len(event_list) == 1: # error checking
        event_list[0].users_going.add(request.user)
        event_list[0].save()
        return HttpResponse('')
    else: 
        return HttpResponse('something failed')

# Update given event to show the user isn't going
def user_cancelled(request):
    event_list = list(Event.objects.filter(id=request.GET.get("event_id")))
    if len(event_list) == 1: # error checking
        event_list[0].users_going.remove(request.user)
        event_list[0].save()
        return HttpResponse('')
    else: 
        return HttpResponse('something failed')

# Return the number of users going to a given event
def get_number_going(request):
    event_list = list(Event.objects.filter(id=request.GET.get("event_id")))    
    if len(event_list) == 1: # error checking
        data = {
            'number_going': event_list[0].users_going.count(),
        }
        return JsonResponse(data)
    else:
        return HttpResponse('something failed')

# Delete a given event from DB
def delete_event(request):
    Event.objects.filter(id=request.GET.get("event_id")).delete()
    return HttpResponse('')