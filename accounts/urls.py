from django.urls import path
from .views import SigupView


urlpatterns = [
    path('signup/', SigupView.as_view(), name='signup'),
]
