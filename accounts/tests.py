from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import resolve, reverse
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .views import ProfileView, SigupView

CustomUser = get_user_model()


class CustomUserTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='test',
            email='test@gmail.com',
            password='test123'
        )
        
        self.super_user = CustomUser.objects.create_superuser(
            username='admin',
            email='admin@gmail.com',
            password='admin123'
        )
        
        
    def test_user_creation(self):
        self.assertEqual(self.user.username, 'test')
        self.assertEqual(self.user.email, 'test@gmail.com')
        self.assertFalse(self.user.is_superuser)
        self.assertTrue(self.user.is_active)
    
    def test_super_user_creation(self):
        self.assertEqual(self.super_user.username, 'admin')
        self.assertEqual(self.super_user.email, 'admin@gmail.com')
        self.assertTrue(self.super_user.is_superuser)
        self.assertTrue(self.super_user.is_active)


class SignupTest(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.answer = self.client.get(url)
    
    def test_signup_page_name(self):
        self.assertEqual(self.answer.status_code, 200)
    
    def test_signup_page_template(self):
        self.assertTemplateUsed(self.answer, 'registration/signup.html')
        self.assertContains(self.answer, 'Signup')
    
    def test_signup_page_form_used(self):
        form = self.answer.context['form']
        self.assertIsInstance(form, CustomUserCreationForm)
    
    def test_signup_page_view_used(self):
        view = resolve(reverse('signup'))
        self.assertEqual(view.func.__name__, SigupView.as_view().__name__)

class ProfileTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', email='test@gmail.com', password='test123')
        
        self.client.login(username='test', password='test123')
        url = reverse('profile', args=[self.user.pk])
        self.answer = self.client.get(url)
    
    def test_profile_page_name(self):
        self.assertEqual(self.answer.status_code, 200)
    
    def test_profile_page_template(self):
        self.assertTemplateUsed(self.answer, 'registration/profile.html')
        self.assertContains(self.answer, 'Profile')
    
    def test_profile_page_form_used(self):
        form = self.answer.context['form']
        self.assertIsInstance(form, CustomUserChangeForm)
    
    def test_profile_page_view_used(self):
        view = resolve(reverse('profile', args=['1']))
        self.assertEqual(view.func.__name__, ProfileView.as_view().__name__)
