# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username',
                  'email',
                  'first_name',
                  'last_name')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('first_name',
                  'last_name',
                  'username')

class UsernameChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username',)

class NameChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('first_name',
                  'last_name',)


class AddFriendForm(forms.Form):
    username = forms.CharField(label="Username", max_length=50)


class RemoveFriendForm(forms.Form):
    username = forms.CharField(label="Username", max_length=50)

