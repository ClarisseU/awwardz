from django import forms
from .models import Projects, Profile

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Projects
        exclude = []
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','project']       
        