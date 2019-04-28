import django
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.template.context_processors import csrf
from django.middleware.csrf import get_token
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from friendship.models import Friend
from bootstrap_datepicker_plus import DateTimePickerInput
from users.forms import CustomUserChangeForm, UsernameChangeForm, NameChangeForm
from .forms import CreateEvent
from .models import Event
from emoji_picker.widgets import EmojiPickerTextInput
from haystack.query import SearchQuerySet
from datetime import *
from django.utils import timezone
import pytz

def testing(request):
    return render(request, 'testing.html')

def upcoming(request):
    rendered = render_to_string('upcoming.html', request=request)
    data = {
        'page': rendered,
    }
    return JsonResponse(data)

def upcoming_events(request):
    events = Event.objects.all()
    upcoming = []
    for event in events:
        if request.user in event.users_going.all():
            if datetime.now().date() <= event.date:
                upcoming.append(event)
    return render_to_response('upcoming-events.html', {'upcoming': upcoming})

def friends_view_site(request):
    rendered = render_to_string('friends/friends_view_site.html', request=request)
    data = {
        'page': rendered,
    }
    return JsonResponse(data)

def friends_view(request):
    friends = Friend.objects.friends(request.user)
    return render_to_response('friends/friends_view.html', {'friends': friends})

# Dynamically return events that match the search
def event_search(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
    else:
        search_text = ''
    
    if (search_text == ''):
        events = None
    else:
        # return all queries that match the search
        event_search_all = SearchQuerySet().models(Event).autocomplete(text=search_text)
        friends = Friend.objects.friends(request.user)
        events = []
        for event in event_search_all:

            # do not show event if it private and not created by the user or their friends
            if event.public or event.created_by != request.user or event.created_by in friends:
                # check if event has already passed
                if timezone.is_aware(event.date):
                    if timezone.now() <= event.date:
                        events.append(event)
                else:
                    if datetime.now() <= event.date:
                        events.append(event)

    return render_to_response('ajax-search.html', {'events': events})

# Load search bar in sidebar for searching for events
def load_event_search(request):
    args = {}
    args.update(csrf(request))
    rendered = render_to_string('event-search.html', args)
    data = {
        'page': rendered
    }
    return JsonResponse(data)

# Dynamically update sidebar with all users going
def whos_going(request):
    event_list = list(Event.objects.filter(id=request.GET.get("event_id")))

    if len(event_list) != 1: # error checking
        return HttpResponse('something failed')
    else: 
        rendered = render_to_string('whos-going.html', {'users_going': event_list[0].users_going.all()})
        data = {
            'page': rendered,
        }
        return JsonResponse(data)


def friends_going(request):
    event_list = list(Event.objects.filter(id=request.GET.get("event_id")))
    if len(event_list) != 1: # error checking
        return HttpResponse('something failed')
    else:
        friends = Friend.objects.friends(request.user)
        users_going = event_list[0].users_going.all()
        friends_user_going = []

        for user in users_going:
            if user in friends:
                friends_user_going.append(user)

        rendered = render_to_string('friends-going.html', {'friends_going': friends_user_going})
        data = {
            'page': rendered,
        }
        return JsonResponse(data)

def ajax_add_event(request):
    event_form = CreateEvent()
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
    return JsonResponse({'page': rendered})

def ajax_edit_profile(request):
    form = CustomUserChangeForm()
    field = request.GET.get("field")[8:]
    rendered = render_to_string('profile/profile_edit.html', {'form': form, 'field': field}, request=request)
    return JsonResponse({'page': rendered})

def ajax_friends_sb(request):
    rendered = render_to_string('friends/friends_sb.html', request=request)
    data = {
        'page': rendered,
    }
    return JsonResponse(data)

def ajax_friends_add(request):
    rendered = render_to_string('friends/friends_add.html', request=request)
    data = {
        'page': rendered,
    }
    return JsonResponse(data)

def ajax_friends_remove(request):
    rendered = render_to_string('friends/friends_remove.html', request=request)
    data = {
        'page': rendered,
    }
    return JsonResponse(data)

def ajax_friends_requests(request):
    rendered = render_to_string('friends/friends_requests.html', request=request)
    data = {
        'page': rendered,
    }
    return JsonResponse(data)

def default_map(request):
    # User changed their profile
    if request.method == 'POST':
        if ("username" in request.POST) or ("first_name" in request.POST) or ("last_name" in request.POST):
            if "username" in request.POST:
                form = UsernameChangeForm(request.POST, instance=request.user)
                if form.is_valid():
                    request.user.username = form.cleaned_data['username']
                    request.user.save()
            elif ("last_name" in request.POST) and ("first_name" in request.POST):
                form = NameChangeForm(request.POST)
                if form.is_valid():
                    request.user.first_name = form.cleaned_data['first_name']
                    request.user.last_name = form.cleaned_data['last_name']
                    request.user.save()
            return HttpResponseRedirect('/')            
        
        # User created an event
        else:
            event_form = CreateEvent(request.POST)
            if event_form.is_valid():
                csrf_token   = get_token(request)
                event_descr  = event_form.cleaned_data['event_descr']
                event_name   = event_form.cleaned_data['event_name']
                event_type   = event_form.cleaned_data['event_type']
                public       = event_form.cleaned_data['public']
                date         = event_form.cleaned_data['date']
                start_time   = event_form.cleaned_data['start_time']
                end_time   = event_form.cleaned_data['end_time']
                location     = event_form.cleaned_data['location']
                lat          = event_form.cleaned_data['lat']
                lng          = event_form.cleaned_data['lng']
                user         = request.user
                new_event = Event(event_name=event_name, event_type=event_type, public=public, date=date, start_time=start_time, end_time=end_time, event_descr=event_descr, location=location, lat=lat, lng=lng, user=user)
                new_event.save()
                new_event.users_going.add(user)

                # Send user to home page
                return HttpResponseRedirect('/')
    
    # User requested the home page via GET
    elif request.method == 'GET':
        return render(request, 'main.html', {'mapbox_access_token': 'pk.eyJ1IjoiY29zMzMzIiwiYSI6ImNqdDYzY3A0ZDBkMGc0YXF4azczdXRheWMifQ.3VeYeV_c-231Lab62H2XtQ'})

# Return all events from the database as a JSON object
def fetch_from_db(request):
    all_events = Event.objects.all()
    data = {
        'events':{}
    }
    for event in all_events:
        # Set a boolean value if the logged-in user is going to a given event
        users_going = []
        going = False
        for user_going in event.users_going.all():
            if user_going.id == request.user.id:
                going = True
            users_going.append(user_going.first_name + " " + user_going.last_name)
        number_going = event.users_going.count()

        # See if the logged in user should be able to see the event
        if event.public:
            should_display = True
        elif event.user == request.user:
            should_display = True
        elif Friend.objects.are_friends(request.user, event.user):
            should_display = True
        else:
            should_display = False

        
        dict = {
            'number_going': number_going,
            'user_going': going,
            'users_going': users_going,
            'should_display': should_display,
            'event_id':event.id,
            'date': event.date,
            'start_time': event.start_time,
            'end_time': event.end_time,
            'created_by': event.user == request.user, # if user created given event
            'event_descr': event.event_descr,
            'event_type': event.event_type,
            'location': event.location,
            'lng': event.lng,
            'lat': event.lat,
        }

        if (datetime.now().date() <= event.date):
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