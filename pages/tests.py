from django.test import TestCase, SimpleTestCase
from .views import HomePageView
from django.urls import reverse, resolve


class HomePageTest(SimpleTestCase):
    def setUp(self):
        url = reverse('home')
        self.answer = self.client.get(url)
    
    def test_home_page_name(self):
        self.assertEqual(self.answer.status_code, 200)
    
    def test_home_page_template(self):
        self.assertTemplateUsed(self.answer, 'index.html')
        self.assertContains(self.answer, 'Pagina Inicial')
    
    def test_home_page_view(self):
        view = resolve(reverse('home'))
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)

