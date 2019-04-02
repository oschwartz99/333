# users/views.py
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from friendship.models import Friend, Block, FriendshipRequest
from friendship.exceptions import AlreadyExistsError, AlreadyFriendsError
from friendship.models import Friend, Follow, Block
from django.contrib.auth import update_session_auth_hash
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm, AddFriendForm, RemoveFriendForm


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def profile_page(request):
    args = {'user': request.user}
    return render(request, 'profile_page.html')


def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': CustomUser.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
    return JsonResponse(data)


def profile_edit(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/users/profile/')
        else:
            return redirect('/users/edit/')
    else:
        form = CustomUserChangeForm(instance=request.user)
        args = {'form': form}
        return render(request, 'profile_edit.html', args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user) # Prevents you from getting logged out
            return redirect('/users/profile/')
        else:
            return redirect('/users/change_password/')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'profile_edit.html', args) # Still uses profile_edit.html as it simply takes a form


def friends_page(request):
    args = {'user': request.user}
    return render(request, 'friends/friends_page.html')


def username_present(username):
    if CustomUser.objects.filter(username=username).exists():
        return True
    return False


def add_friend(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddFriendForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            new_friend_username = form.cleaned_data['username']
            # check whether requested user exists.
            if username_present(new_friend_username):
                new_friend = CustomUser.objects.get(username=new_friend_username)
                # catch error for when friend request has already been sent
                if (not Friend.objects.are_friends(request.user, new_friend)
                        and not Friend.objects.can_request_send(request.user, new_friend)):
                    Friend.objects.add_friend(request.user,  new_friend, message='Hi! I would like to add you')
            # create a blank form
            form = AddFriendForm()
            return render(request, 'friends/add_friend.html', {'form': form})
    else:
        form = AddFriendForm()

    return render(request, 'friends/add_friend.html', {'form': form})


def remove_friend(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RemoveFriendForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            friend_username = form.cleaned_data['username']
            # check whether requested user exists.
            if username_present(friend_username):
                friend = CustomUser.objects.get(username=friend_username)
                # catch error for when friend request has already been sent
                if Friend.objects.are_friends(request.user, friend):
                    Friend.objects.remove_friend(request.user, friend)
            # create a blank form
            form = RemoveFriendForm()
            return render(request, 'friends/remove_friend.html', {'form': form})
    else:
        form = RemoveFriendForm()

    return render(request, 'friends/remove_friend.html', {'form': form})


def accept_friend_request(request):

    return render(request, 'add_friend.html')


def view_friend_requests(request):
    return render(request, 'friends/view_friend_requests.html')


def view_friends(request):
    return render(request, 'friends/view_friends.html')
