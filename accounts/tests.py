from django.test import TestCase
from django.contrib.auth import get_user_model


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

        