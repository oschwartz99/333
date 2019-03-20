# users/views.py
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from .models import CustomUser
from django.http import JsonResponse

from .forms import CustomUserCreationForm

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def profile_page(request):
    return render(request, 'profile_page.html')

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': CustomUser.objects.filter(username__iexact=username).exists()
    }
    print(data)
    return JsonResponse(data)
