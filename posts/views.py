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
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class EditPostItem(UpdateView):
    model = Post
    fields = ['title', 'content', 'image']
    def get_queryset(self):
        print(self.request.user.is_superuser)
        base_qs = super(EditPostItem, self).get_queryset()
        return base_qs.filter(author=self.request.user)
        
class DeletePostItem(DeleteView):
    model = Post
    success_url = reverse_lazy('posts')
    def get_queryset(self):
        base_qs = super(DeletePostItem, self).get_queryset()
        return base_qs.filter(author=self.request.user)