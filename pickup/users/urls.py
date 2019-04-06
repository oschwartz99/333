# users/urls.py
from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    url('profile/', views.profile_page, name='profile_page'),
    url('ajax/validate_username/', views.validate_username, name='validate_username'),
    url('ajax/validate_email/', views.validate_email, name='validate_email'),
    url('edit/', views.profile_edit, name='profile_edit'),
    url('password/', views.change_password, name='change_password'),
    url('friends/', views.friends_page, name='friends'),
    url('add_friend/', views.add_friend, name='add_friend'),
    url('view_friend_requests', views.view_friend_requests, name='view_friend_requests'),
    url('view_friends', views.view_friends, name='view_friends'),
    url('remove_friend/', views.remove_friend, name='remove_friend')
]
