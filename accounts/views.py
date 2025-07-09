from django.shortcuts import render
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import get_user_model
from django.views.generic import CreateView, UpdateView


class SigupView(CreateView):
    model = get_user_model()
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm
    

class ProfileView(UpdateView):
    model = get_user_model()
    template_name = 'registration/profile.html'
    form_class = CustomUserChangeForm
