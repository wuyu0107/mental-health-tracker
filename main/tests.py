from django.test import TestCase, Client
from django.utils import timezone
from .models import MoodEntry
from django.contrib.auth.models import User  # Import the User model

class MainTest(TestCase):
    def setUp(self):
        # Create and log in a test user for tests that require authentication
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
    
    def test_main_url_is_exist(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/skibidi/')
        self.assertEqual(response.status_code, 404)

    def test_strong_mood_user(self):
        user = self.user
        now = timezone.now()
        mood = MoodEntry.objects.create(
            user=user,
            mood="Happy",
            time = now,
            feelings = "I'm happy, even though my clothes are soaked from the rain :(",
            mood_intensity = 8,
        )
        self.assertEqual(mood.user, user)
        self.assertTrue(mood.is_mood_strong)

    def test_main_template_uses_correct_page_title(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        html_response = response.content.decode("utf8")
        self.assertIn("PBD Mental Health Tracker", html_response)
    
    def test_main_using_main_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, 'main.html')
