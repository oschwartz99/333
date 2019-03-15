from django.conf.urls import url                                                                                                                              
from . import views

urlpatterns = [ 
    url('testing/list_events/', views.testing_list_events, name = "list_events"),
    url('testing/', views.testing_view, name="testing"),
    url('', views.default_map, name="maps"),
]