from django.urls import path
from .views import ListCoursesView, CourseDetailsView, CreateCourseView

urlpatterns = [
    path('list/', ListCoursesView.as_view(), name='list_courses'),
    path('course_details/<int:pk>/', CourseDetailsView.as_view(), name='course_details'),
    path('create_course/', CreateCourseView.as_view(), name='create_course'),
]
