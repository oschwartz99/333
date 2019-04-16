# users/views.py
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, login
from friendship.models import Friend, Block, FriendshipRequest
from friendship.exceptions import AlreadyExistsError, AlreadyFriendsError
from friendship.models import Friend, Follow, Block
from django.contrib.auth import update_session_auth_hash
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm, AddFriendForm, RemoveFriendForm
from .tokens import account_activation_token
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your Pickup account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('You need to verify your email address - check your email for an email from our team.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('maps')
    else:
        return HttpResponse('Activation link is invalid!')

def profile_page(request):
    args = {'user': request.user}
    return render(request, 'profile_page.html')


def validate_username(request):
    print("validating!")
    username = request.GET.get('username', None)
    data = {
        'is_taken': CustomUser.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
    return JsonResponse(data)


def validate_email(request):
    email = request.GET.get('email', None)
    data = {
        'is_taken': CustomUser.objects.filter(email__iexact=email).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this email already exists.'
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
        return render(request, 'profile_password.html', args)


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
                    Friend.objects.add_friend(request.user,  new_friend, new_friend_username)
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


def accept_friend(request, pk):
    other_user = CustomUser.objects.get(pk=pk)
    FriendshipRequest.objects.filter(
        from_user=request.user,
        to_user=other_user
    ).delete()
    FriendshipRequest.objects.filter(
        from_user=other_user,
        to_user=request.user
    ).delete()

    Friend.objects.add_friend(request.user, other_user, "")

    friend_request = FriendshipRequest.objects.get(to_user=pk)
    friend_request.accept()

    return render(request, 'friends/view_friends.html')


def decline_friend(request, pk):
    other_user = CustomUser.objects.get(pk=pk)
    FriendshipRequest.objects.filter(
        from_user=request.user,
        to_user=other_user
    ).delete()
    FriendshipRequest.objects.filter(
        from_user=other_user,
        to_user=request.user
    ).delete()

    Friend.objects.add_friend(request.user, other_user, "")

    friend_request = FriendshipRequest.objects.get(to_user=pk)
    friend_request.reject()

    return render(request, 'friends/view_friends.html')


def view_friend_requests(request):

    friend_requests = Friend.objects.unrejected_requests(user=request.user)

    friend_requests_users = []
    for friend_request in friend_requests:
        friend_requests_users.append(friend_request)

    return render(request, 'friends/view_friend_requests.html', {'friend_requests': friend_requests})


def view_friends(request):
    friends = Friend.objects.friends(request.user)

    return render(request, 'friends/view_friends.html', {'friends': friends})
