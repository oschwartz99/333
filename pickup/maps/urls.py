from django.conf.urls import url                                                                                                                              
from . import views

urlpatterns = [ 
    url('testing/', views.testing_view, name="testing"),
    url('', views.default_map, name="maps"),
]