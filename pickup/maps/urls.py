from django.conf.urls import url                                                                                                                              
from . import views

print('in maps urls')

urlpatterns = [ 
    url('testing/', views.testing_view, name="testing"),
    url('', views.default_map, name="maps"),
]