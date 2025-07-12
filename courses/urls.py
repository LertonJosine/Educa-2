from django.urls import path
from .views import ListCoursesView

urlpatterns = [
    path('list/', ListCoursesView.as_view(), name='list_courses')
]
