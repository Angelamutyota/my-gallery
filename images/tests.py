from django.test import TestCase
from .models import Image, Category, Location

# Create your tests here.
class LocationTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.nairobi = Location(name= 'Nairobi')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi,Location))
    # Testing Save Method
    def test_save_method(self):
        self.nairobi.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

class ImageTestClass(TestCase):
    def setUp(self):
        # Creating a new location and saving it
        self.nairobi = Location(name= 'Nairobi')
        self.nairobi.save_location()

        self.nature = Category(name= 'nature')
        self.nature.save_category()


        self.new_image= Image(image='image.jpg', name = 'imagetest', desc= 'this is a test', loc= self.nairobi, category= self.nature)
        self.new_image.save()


    
      
