from django.urls import path
from .views import SigupView, ProfileView


urlpatterns = [
    path('signup/', SigupView.as_view(), name='signup'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
]
