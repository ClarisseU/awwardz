from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Projects(models.Model):
    title= models.CharField(max_length=60, null=True)
    screenshot = models.ImageField(upload_to='image/', null=True)
    description = models.CharField(max_length=60, null=True)
    link = HTMLField()
    user= models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    design = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0, null= True)
    usability = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0, null= True)
    content = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0, null= True)
    vote_submissions = models.IntegerField(default=0, null= True)
    
    def __str__(self):
        return str(self.title)
    
    def save_project(self):
        self.save()
     
    @classmethod    
    def search_by_title(cls, search_term):
        title = cls.objects.filter(title__icontains=search_term)
        return title
    
    @classmethod
    def get_all_projects(cls):
        project = cls.objects.all().prefetch_related('comments_set')
    
    
class Profile(models.Model):
    picture = models.ImageField(upload_to='profile/', null=True)
    bio = models.CharField(max_length=60, null=True)
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.bio)
    
    def save_profile(self):
        self.save()
        
class Comments(models.Model):
    comment_cont = models.CharField(max_length=120)
    commented_by = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    commented_project = models.ForeignKey(Projects, on_delete=models.CASCADE, null=True)
            

class Review(models.Model):
    pass

