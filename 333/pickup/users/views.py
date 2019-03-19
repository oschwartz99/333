# users/views.py
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth.models  import User
from django.contrib.auth.forms import UserChangeForm
from .forms import CustomUserCreationForm

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def profile_page(request):
    args = {'user': request.user}
    return render(request, 'profile_page.html')

def profile_edit(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/users/profile/')
    else:
        form = UserChangeForm(instance=request.user)
        args = {'form': form}
        return render(request, 'profile_edit.html', args)
