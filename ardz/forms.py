from django import forms
from .models import Projects, Profile, Comments

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Projects
        exclude = []
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','project']       
        
class commentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['commented_by','commented_project']           