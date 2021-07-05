from django.test import TestCase
from .models import Image, Category, Location

# Create your tests here.
class LocationTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.nairobi = Location(name= 'Nairobi')
