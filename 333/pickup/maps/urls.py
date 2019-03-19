from django.conf.urls import url                                                                                                                              
from . import views

urlpatterns = [ 
    url('testing/list_events/', views.testing_list_events, name = "list_events"),
    url('testing/map_def', views.testing_map_def, name='map_def'),
    url('testing/', views.testing_view, name="testing"),
    url('', views.default_map, name="maps"),
]