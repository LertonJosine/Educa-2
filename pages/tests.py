from django.test import TestCase, SimpleTestCase
from .views import HomePageView, TrainersView, AboutPageView
from django.urls import reverse, resolve


class HomePageTest(SimpleTestCase):
    def setUp(self):
        url = reverse('home')
        self.answer = self.client.get(url)
    
    def test_home_page_name(self):
        self.assertEqual(self.answer.status_code, 200)
    
    def test_home_page_template(self):
        self.assertTemplateUsed(self.answer, 'index.html')
    
    def test_home_page_view(self):
        view = resolve(reverse('home'))
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)


class TrainersPageTest(SimpleTestCase):
    def setUp(self):
        url = reverse('trainers')
        self.answer = self.client.get(url)
    
    def test_trainers_page_name(self):
        self.assertEqual(self.answer.status_code, 200)
    
    def test_trainers_page_template(self):
        self.assertTemplateUsed(self.answer, 'trainers.html')
        self.assertContains(self.answer, 'Trainers')
    
    def test_trainers_page_view(self):
        view = resolve(reverse('trainers'))
        self.assertEqual(view.func.__name__, TrainersView.as_view().__name__)


class AboutPageTest(SimpleTestCase):
    def setUp(self):
        url = reverse('about')
        self.answer = self.client.get(url)
    
    def test_about_page_name(self):
        self.assertEqual(self.answer.status_code, 200)
    
    def test_about_page_template(self):
        self.assertTemplateUsed(self.answer, 'about.html')
        self.assertContains(self.answer, 'About')
    
    def test_about_page_view(self):
        view = resolve(reverse('about'))
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)
