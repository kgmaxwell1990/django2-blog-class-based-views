from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
        
class ShowPostList(ListView):
    model = Post
    
class ShowPostItem(DetailView):
    model = Post
    
class AddPostItem(CreateView):
    model = Post
    fields = ['title', 'content', 'image']
    
class EditPostItem(UpdateView):
    model = Post
    fields = ['title', 'content', 'image']

class DeletePostItem(DeleteView):
    model = Post
    success_url = reverse_lazy('posts')