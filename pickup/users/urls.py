# users/urls.py
from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    url('profile/', views.profile_page, name='profile_page'),
    url('edit/', views.profile_edit, name='profile_edit')
]
