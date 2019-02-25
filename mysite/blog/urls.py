from django.urls import path
from . import views

urlpatterns = [
    # maps to home function in views.py
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
