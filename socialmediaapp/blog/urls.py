"""socialmediaapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from django.conf import settings
from django.views.static import serve
from .import views
from .views import (
    PostListView,
    PostCreateView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView,
    AllPostListView,
    SaveView,
    AddCommentView
 )

urlpatterns = [
    path('', AllPostListView.as_view(), name='blog-allposts'),
    path('myposts/', PostListView.as_view(), name='blog-home'),
    path('savedposts/', views.saved_posts, name='blog-saved'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>', SaveView, name='post-save'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('friendposts/', views.posts_of_following_profiles, name='blog-about'),
    path('tags/<int:pk>', views.tagged_posts, name='blog-tags'),
    path('searchposts/', views.searchposts, name='blog-search'),
    path('post/<int:pk>/comment/', AddCommentView.as_view(), name='add-comment'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
