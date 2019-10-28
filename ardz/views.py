from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Profile, Projects, Comments
from .forms import NewPostForm, ProfileForm,commentForm,VoteForm
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer, ProjectSerializer


# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    project = Projects.objects.all()
    avg=0
    current_user = request.user
    user_profile = Profile.objects.all()
    profile = Profile.objects.filter(id=current_user.id).first()
    comment = Comments.objects.filter(id = current_user.id).first()
    for p in projects:
        avg = (p.design + p.usability + p.content)/3
        rating = round(avg,2)
    
    return render(request, 'index.html', {'project':project,'user_profile':user_profile, 'profile': profile, 'comment':comment, 'rating':rating})
    
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

@login_required(login_url='/accounts/login')
def comment(request, id):
    current_user = request.user
    project = Projects.objects.filter(id = id).first()
    print(project)
    prfl = Profile.objects.filter(user = current_user.id).first()
    print(prfl)
    if request.method == 'POST':
        form = commentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.commented_by = prfl
            comment.commented_project = project
            comment.save()
            return redirect('welcome')
    else:
        form = commentForm()
    return render(request, 'commentform.html', {'form': form, 'id':id})
        
#found the code on github of the username:'MaryannGitonga'
@login_required(login_url='/accounts/login/')
def rating(request,id):
    project=Projects.objects.get(id=id)
    rating = round(((project.design + project.usability + project.content)/3),1)
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid:
            project.vote_submissions += 1
            if project.design == 0:
                project.design = int(request.POST['design'])
            else:
                project.design = (project.design + int(request.POST['design']))/2
            if project.usability == 0:
                project.usability = int(request.POST['usability'])
            else:
                project.usability = (project.design + int(request.POST['usability']))/2
            if project.content == 0:
                project.content = int(request.POST['content'])
            else:
                project.content = (project.design + int(request.POST['content']))/2
            project.save()
            return redirect('welcome')
    else:
        form = VoteForm()
    return render(request,'voting.html',{'form':form,'project':project,'rating':rating})         