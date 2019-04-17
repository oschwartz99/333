# users/urls.py
from django.urls import path, include
from . import views
from django.conf.urls import url

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url('profile/', views.profile_page, name='profile_page'),
    url('ajax/validate_username/', views.validate_username, name='validate_username'),
    url('ajax/validate_email/', views.validate_email, name='validate_email'),
    url('edit/', views.profile_edit, name='profile_edit'),
    url('password/', views.change_password, name='change_password'),
    url('friends/', views.friends_page, name='friends'),
    url('search_users/', views.search_users, name='search_users'),
    url(r'add_friend/(?P<pk>\d+)/', views.add_friend, name='add_friend'),
    url('view_friend_requests', views.view_friend_requests, name='view_friend_requests'),
    url('view_friends', views.view_friends, name='view_friends'),
    url('remove_friend/', views.remove_friend, name='remove_friend'),
    url(r'accept_friend/(?P<pk>\d+)/', views.accept_friend, name='accept_friend'),
    url(r'decline_friend/(?P<pk>\d+)/', views.decline_friend, name='decline_friend'),
    url(r'search/', include('haystack.urls')),
]
