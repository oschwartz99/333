from django.conf.urls import url   
from djgeojson.views import GeoJSONLayerView                                                                                                                           
from . import views

urlpatterns = [ 
    url('ajax/fetch_from_db/', views.fetch_from_db, name='fetch_from_db'),    
    url('ajax/user_going/', views.user_going, name='user_going'),
    url('ajax/delete_event/', views.delete_event, name='delete_event'),
    url('ajax/user_cancelled/', views.user_cancelled, name='user_cancelled'),
    url('ajax/get_number_going/', views.get_number_going, name='get_number_going'),
    url('add_event/list_events/', views.list_events, name = "list_events"),
    url('add_event/', views.add_event, name="add_event"),
    url('', views.default_map, name="maps"),
]