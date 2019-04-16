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

# Dynamically return events that match the search
def event_search(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
    else:
        search_text = ''
    
    if (search_text == ''):
        events = None
    else: events = Event.objects.filter(event_name__contains=search_text) | \
             Event.objects.filter(event_descr__contains=search_text) | \
             Event.objects.filter(location__contains=search_text)
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
        users_going = event_list[0].users_going.all()
        rendered = render_to_string('whos-going.html', {'users_going': users_going})
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

def default_map(request):
    # User changed their profile
    if request.method == 'POST':
        if ("username" in request.POST) or ("first_name" in request.POST) or ("last_name" in request.POST):
            if "username" in request.POST:
                form = UsernameChangeForm(request.POST)
                if form.is_valid():
                    request.user.username = form.cleaned_data['username']
                    request.user.save()
                    print("saved!")
            elif ("last_name" in request.POST) and ("first_name" in request.POST):
                form = NameChangeForm(request.POST)
                if form.is_valid():
                    request.user.first_name = form.cleaned_data['first_name']
                    request.user.last_name = form.cleaned_data['last_name']
                    request.user.save()
                    print('saved!')
            return HttpResponseRedirect('/')            
        
        # User created an event
        else:
            event_form = CreateEvent(request.POST)
            if event_form.is_valid():
                csrf_token   = get_token(request)
                event_descr = event_form.cleaned_data['event_descr']
                event_name   = event_form.cleaned_data['event_name']
                event_type   = event_form.cleaned_data['event_type']
                public       = event_form.cleaned_data['public']
                datetime    = event_form.cleaned_data['datetime']
                location     = event_form.cleaned_data['location']
                lat          = event_form.cleaned_data['lat']
                lng          = event_form.cleaned_data['lng']
                user         = request.user
                new_event = Event(event_name=event_name, event_type=event_type, public=public, datetime=datetime, event_descr=event_descr, location=location, lat=lat, lng=lng, user=user)
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