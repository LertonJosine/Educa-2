from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class CustomUserModel(AbstractUser):
    
    def get_absolute_url(self):
        return reverse("login")
    


