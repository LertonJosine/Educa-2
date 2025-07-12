from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class CustomUserModel(AbstractUser):
    profile_image = models.FileField(upload_to='accounts/profile/img/', default='trainer-2.jpg')
    def get_absolute_url(self):
        return reverse("login")
    


