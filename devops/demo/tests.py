# demo/tests.py
from django.test import TestCase, Client
from django.urls import reverse
# Import your models if you need to test them
# from .models import YourModel

class ViewTests(TestCase):
    """Tests for the views in the demo app"""
    
    def setUp(self):
        """Set up data for the tests"""
        # Create test data if needed
        # Example: self.user = User.objects.create_user(username='testuser', password='12345')
        self.client = Client()
        
    def test_home_page(self):
        """Test that the home page loads correctly"""
        # Get the URL for the view using reverse
        url = reverse('home')  # Replace 'home' with your actual URL name
        response = self.client.get(url)
        
        # Check that the response is 200 OK
        self.assertEqual(response.status_code, 200)
        
        # Check that the page contains expected content
        self.assertContains(response, 'Welcome')  # Adjust for your actual content
        
class ModelTests(TestCase):
    """Tests for models in the demo app"""
    
    def setUp(self):
        """Set up test data"""
        # Create test model instances
        # Example: self.item = YourModel.objects.create(name='Test Item')
        pass
        
    def test_model_str(self):
        """Test the string representation of models"""
        # Example: self.assertEqual(str(self.item), 'Test Item')
        pass
        
    def test_model_methods(self):
        """Test custom model methods"""
        # Example: self.assertEqual(self.item.get_absolute_url(), '/items/1/')
        pass