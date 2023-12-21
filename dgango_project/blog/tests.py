from django.test import TestCase
from django.contrib.auth.models import User
from .models import Review, Places

class YourAppTestCase(TestCase):
    def setUp(self):
        # Set up any initial data or state needed for the tests
        self.user = User.objects.create(username='testuser', password='testpassword')
        self.place = Places.objects.create(pName='Test Place', types='Test Type', pImage='test_image.jpg', rate=4)

    def test_review_creation(self):
        # Test creating a review
        review = Review.objects.create(comment='Test Comment', author=self.user, place=self.place, rate=5)
        
        # Check if the review was created successfully
        self.assertEqual(Review.objects.count(), 1)
        self.assertEqual(review.comment, 'Test Comment')
        self.assertEqual(review.author, self.user)
        self.assertEqual(review.place, self.place)
        self.assertEqual(review.rate, 5)

    def test_place_avg_rating(self):
        # Test the get_avg_rating method of the Places model
        review1 = Review.objects.create(comment='Review 1', author=self.user, place=self.place, rate=4)
        review2 = Review.objects.create(comment='Review 2', author=self.user, place=self.place, rate=5)
        

    # Add more test methods as needed for your application

