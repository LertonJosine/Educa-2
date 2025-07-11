from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Course(models.Model):
    name = models.CharField(max_length=150)
    trainer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.FileField(upload_to='course/covers')
    sits = models.IntegerField()
    resume = models.TextField()
    
    def __str__(self):
        return self.name[:100]
    
    def get_absolute_url(self):
        return reverse("home")
    