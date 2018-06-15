from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.utils import timezone
from .models import Post
        
class ShowAllPosts(ListView):
    model = Post
    
    
class ShowPost(DetailView):
    model = Post
