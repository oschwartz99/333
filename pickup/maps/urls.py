from django.conf.urls import url   
from djgeojson.views import GeoJSONLayerView                                                                                                                           
from . import views

urlpatterns = [ 
    url('ajax/fetch_from_db/', views.fetch_from_db, name='fetch_from_db'),    
    url('ajax/user_going/', views.user_going, name='user_going'),
    url('ajax/delete_event/', views.delete_event, name='delete_event'),
    url('ajax/user_cancelled/', views.user_cancelled, name='user_cancelled'),
    url('ajax/get_number_going/', views.get_number_going, name='get_number_going'),
    url('testing/list_events/', views.testing_list_events, name = "list_events"),
    url('testing/map_def', views.testing_map_def, name='map_def'),
    url('testing/', views.testing_view, name="testing"),
    url('', views.default_map, name="maps"),
]