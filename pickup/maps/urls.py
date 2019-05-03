from django.conf.urls import url   
from djgeojson.views import GeoJSONLayerView                                                                                                                           
from . import views
from django.urls import include


urlpatterns = [ 
    url('ajax/upcoming/', views.upcoming, name='upcoming'),
    url('ajax/upcoming_events/', views.upcoming_events, name='upcoming_events'),
    url('ajax/add_event/', views.ajax_add_event, name='ajax_add_event'),
    url('ajax/profile_sb/', views.ajax_profile_sb, name='ajax_profile_sb'),
    url('ajax/edit_profile/', views.ajax_edit_profile, name='ajax_edit_profile'),
    url('ajax/friends_sb/', views.ajax_friends_sb, name='ajax_friends_sb'),
    url('ajax/friends_view_site/', views.friends_view_site, name='friends_view_site'),
    url('ajax/friends_view/', views.friends_view, name='friends_view'),
    url('ajax/friends_requests_site/', views.friends_requests_site, name='friends_requests_site'),
    url('ajax/friends_requests/', views.friends_requests, name='friends_requests'),
    url('ajax/friends_remove/', views.ajax_friends_remove, name='ajax_friends_remove'),
    url('ajax/home_sb/', views.ajax_home_sb, name='ajax_main_sb'),         
    url('ajax/fetch_from_db/', views.fetch_from_db, name='fetch_from_db'),    
    url('ajax/user_going/', views.user_going, name='user_going'),
    url('ajax/delete_event/', views.delete_event, name='delete_event'),
    url('ajax/user_cancelled/', views.user_cancelled, name='user_cancelled'),
    url('ajax/get_number_going/', views.get_number_going, name='get_number_going'),
    url('ajax/whos_going/', views.whos_going, name='whos_going'),
    url('ajax/friends_going/', views.friends_going, name='friends_going'),
    url('ajax/load_event_search/', views.load_event_search, name='load_event_search'),
    url('ajax/event_search/', views.event_search, name='event_search'),
    url('ajax/load_friends_search/', views.load_friends_search, name='load_friends_search'),
    url('ajax/friends_search/', views.friends_search, name='friends_search'),
    url('ajax/send_req/', views.send_req, name='send_req'),
    url('ajax/accept_req/', views.accept_req, name='accept_req'),
    url('ajax/reject_req/', views.reject_req, name='reject_req'),
    url("testing/", views.testing, name="testing"),
    url('', views.default_map, name="maps"),
]