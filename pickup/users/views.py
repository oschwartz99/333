# users/views.py
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from .models import CustomUser
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models  import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import update_session_auth_hash

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