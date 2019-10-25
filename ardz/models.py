from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Projects(models.Model):
    title= models.CharField(max_length=60, null=True)
    landing_image = models.ImageField(upload_to='image/', null=True)
    description = models.CharField(max_length=60, null=True)
    link = HTMLField()
    
    def __str__(self):
        return str(self.title)
    
    def save_project(self):
        self.save()
    
    
class Profile(models.Model):
    picture = models.ImageField(upload_to='profile/', null=True)
    bio = models.CharField(max_length=60, null=True)
    project = models.ForeignKey(Projects, null=True)
    user_contact = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.bio)
    
    def save_profile(self):
        self.save()

class Review(models.Model):
    pass
