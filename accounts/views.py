from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from django.views.generic import CreateView


class SigupView(CreateView):
    model = get_user_model()
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm
    
