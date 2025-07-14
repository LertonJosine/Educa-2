from django.test import TestCase
from .views import ListCoursesView, CourseDetailsView, CreateCourseView
from django.urls import reverse, resolve
from .models import Course
from django.contrib.auth import get_user_model


class ListCoursesTest(TestCase):
    def setUp(self):
        url = reverse('list_courses')
        self.answer = self.client.get(url)
    
    def test_list_courses_page_name(self):
        self.assertEqual(self.answer.status_code, 200)
    
    def test_list_courses_page_template(self):
        self.assertTemplateUsed(self.answer, 'list_courses.html')
    
    def test_list_courses_page_view(self):
        view = resolve(reverse('list_courses'))
        self.assertEqual(view.func.__name__, ListCoursesView.as_view().__name__)


class CourseDetailsTest(TestCase):
    def setUp(self):
        self.trainer = get_user_model().objects.create_user(
            username='test',
            email='test@gmail.com'
        )
        self.course = Course.objects.create(
            name='course_test',
            trainer=self.trainer,
            sits=30,
            price=300,
            resume='it is just a test',
            cover='media/course-1.jpg'
        )
        url = reverse('course_details', args=[self.course.pk])
        self.answer = self.client.get(url)
    
    def test_course_details_page_name(self):
        self.assertEqual(self.answer.status_code, 200)
    
    def test_course_details_page_template(self):
        self.assertTemplateUsed(self.answer, 'course_details.html')
        self.assertContains(self.answer, 'Course Details')
    
    def test_course_details_page_view(self):
        view = resolve(reverse('course_details', args=[self.course.pk]))
        self.assertEqual(view.func.__name__, CourseDetailsView.as_view().__name__)


class CreateCourseTest(TestCase):
    def setUp(self):
        self.superuser = get_user_model().objects.create_superuser(
            username='superuser',
            email='admin@gmail.com',
            password='admin123'
        )
        self.client.login(username='superuser', password='admin123')
        url = reverse('create_course')
        self.answer = self.client.get(url)
    
    def test_create_course_page_name(self):
        self.assertEqual(self.answer.status_code, 200)
    
    def test_create_course_page_template(self):
        self.assertTemplateUsed(self.answer, 'create_course.html')
        self.assertContains(self.answer, 'Create Course')
    
    def test_create_course_page_view(self):
        view = resolve(reverse('create_course'))
        self.assertEqual(view.func.__name__, CreateCourseView.as_view().__name__)
