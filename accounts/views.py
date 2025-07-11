from django.shortcuts import render
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import get_user_model
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class SigupView(CreateView):
    model = get_user_model()
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm
    

class ProfileView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = get_user_model()
    template_name = 'registration/profile.html'
    form_class = CustomUserChangeForm
    
    def test_func(self):
        user = self.request.user
        return user == self.get_object()
