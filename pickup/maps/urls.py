from django.conf.urls import url   
from djgeojson.views import GeoJSONLayerView                                                                                                                           
from . import views
from django.urls import include


urlpatterns = [ 
    url('ajax/add_event/', views.ajax_add_event, name='ajax_add_event'),   
    url('ajax/profile_sb/', views.ajax_profile_sb, name='ajax_profile_sb'),
    url('ajax/edit_profile/', views.ajax_edit_profile, name='ajax_edit_profile'),
    url('ajax/friends_sb/', views.ajax_friends_sb, name='ajax_friends_sb'),
    url('ajax/friends_view/', views.ajax_friends_view, name='ajax_friends_view'),
    url('ajax/friends_add/', views.ajax_friends_add, name='ajax_friends_add'),
    url('ajax/friends_requests/', views.ajax_friends_requests, name='ajax_friends_requests'),
    url('ajax/friends_remove/', views.ajax_friends_remove, name='ajax_friends_remove'),
    url('ajax/home_sb/', views.ajax_home_sb, name='ajax_main_sb'),         
    url('ajax/fetch_from_db/', views.fetch_from_db, name='fetch_from_db'),    
    url('ajax/user_going/', views.user_going, name='user_going'),
    url('ajax/delete_event/', views.delete_event, name='delete_event'),
    url('ajax/user_cancelled/', views.user_cancelled, name='user_cancelled'),
    url('ajax/get_number_going/', views.get_number_going, name='get_number_going'),
    url('ajax/whos_going/', views.whos_going, name='whos_going'),
    url('ajax/load_event_search/', views.load_event_search, name='load_event_search'),
    url('ajax/event_search/', views.event_search, name='event_search'),
    url(r'search/', include('haystack.urls')),
    url("testing/", views.testing, name="testing"),
    url('', views.default_map, name="maps"),
]