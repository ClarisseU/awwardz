from django.test import TestCase
from .models import Profile, Projects, Comments
from django.contrib.auth.models import User

class ProfileTestClass(TestCase):
    '''
    class to test the profile functionality
    '''
    def setUp(self):
        self.user = User.objects.create(id='1', username='iradukunda')
        self.picture = Profile(picture ='profile/', bio ='me', user=self.user)
        
    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))
        self.assertTrue(isinstance(self.picture, Profile)) 

    def test_save_profile(self):
        self.picture.save_profile()
        pic = Profile.objects.all()
        self.assertTrue(len(pic)>0) 
        
class ProjectTestClass(TestCase):
    '''
    class to test the functionalities and instances of projects class
    '''
    def setUp(self):
        self.user = User.objects.create(id='1', username='iradukunda')
        self.profile = Profile.objects.create(picture='picture/', bio='myself', user=self.user)
        self.project = Projects.objects.create(title='project', screenshot='image/', description='true', link='link', user=self.user, design='8', usability='8', content='8',vote_submissions='8' )
        
    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))
        self.assertTrue(isinstance(self.profile, Profile))
        self.assertTrue(isinstance(self.project, Projects))
               
    def test_save_project(self):
        self.project.save_project() 
        proj = Projects.objects.all()
        self.assertTrue(len(proj)>0)   
          