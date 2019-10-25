from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Profile, Projects
from .forms import NewPostForm, ProfileForm
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer, ProjectSerializer


# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    project = Projects.objects.all()
    
    return render(request, 'index.html',{'project':project})
    
@login_required(login_url='/accounts/login')    
def post(request,id):
    try:
        projects= Projects.objects.get(id=id)
    except DoesNotExist:
        raise Http404
    return render(request, 'index.html',{'project':projects})

@login_required(login_url='/accounts/login')
def new_post(request):
    current_user = request.user 
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('welcome')
    else:
        form = NewPostForm()
    return render (request, 'new_post.html', {"form":form})

@login_required(login_url='/accounts/login/')
def search(request):
   if 'title' in request.GET and request.GET["title"]:
       search_term = request.GET.get("title")
       searched_title = Projects.search_by_title(search_term)
       
       message = f"{search_term}"
       return render(request, "search.html",{"message":message,"titles": searched_title})
   else:
       message = "You haven't searched for any term"
       return render(request, 'search.html',{"message":message})
   
@login_required(login_url='/accounts/login')    
def profile(request):
    current_user = request.user
    # picture = Profile.objects.filter(user=current_user).all()
    profiles = Profile.objects.filter(user=current_user).first()
    return render(request, 'profile.html',{'profiles':profiles})

@login_required(login_url='/accounts/login')
def new_profile(request):
    current_user = request.user 
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('welcome')
    else:
        form = ProfileForm()
    return render (request, 'new_profile.html', {"form":form})

class ProfileList(APIView):
    def get(self, request, format=None):
        all_merch = Profile.objects.all()
        serializers = ProfileSerializer(all_merch, many=True)
        return Response(serializers.data)
    
class ProjectList(APIView):
    def get(self, request, format=None):
        all_merch1 = Projects.objects.all()
        serializers = ProjectSerializer(all_merch1, many=True)
        return Response(serializers.data)    
