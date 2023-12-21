from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

class YourAppTestCase(TestCase):
    def setUp(self):
        # Set up any necessary data or objects for your tests
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            email='testuser@example.com'
        )


    def test_user_creation(self):
        # Test user creation
        new_user = User.objects.create_user(
            username='newuser',
            password='newpassword',
            email='newuser@example.com'
        )
        self.assertEqual(new_user.username, 'newuser')
        self.assertTrue(new_user.check_password('newpassword'))


