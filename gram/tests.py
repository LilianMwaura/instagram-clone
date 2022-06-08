from django.test import TestCase
from .models import Image, Comment, Profile, Like
from django.contrib.auth.models import User
        
class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.Prof= Profile(id = '1', profile_photo = 'example.jpg', bio = 'Hi there',)
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Prof,Profile)) 
        
class CommentTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.Comm= Comment(id = '1', comment = 'Hi there',)
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Comm,Comment))    
         

class LikeTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.Lik= Like(id = '1')
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Lik,Like))       


