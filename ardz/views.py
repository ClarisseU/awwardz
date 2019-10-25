from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Profile, Projects

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    project = Projects.objects.all()
    return render(request, 'index.html')
    
