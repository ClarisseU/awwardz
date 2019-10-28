from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^new/post$',views.new_post, name ='new-post'),
    url(r'^search',views.search, name='search'),
    url(r'^new/newprofile$',views.new_profile, name ='new-profile'),
    url(r'^new/profile$',views.profile, name ='profile'),
    url(r'^api/merch/$', views.ProfileList.as_view(), name='profile_api'),
    url(r'^api/merch1/$', views.ProjectList.as_view(), name='project_api'),
    url(r'^new/comment/(\d+)/$',views.comment, name ='comment'),
    url(r'^vote/(?P<id>\d+)',views.rating,name='rating'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)