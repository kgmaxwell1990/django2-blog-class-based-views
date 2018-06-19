from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from django.http import HttpResponseForbidden
        
class ShowPostList(ListView):
    model = Post
    
class ShowPostItem(DetailView):
    model = Post
    
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.views += 1
        obj.save()
        return super(ShowPostItem, self).dispatch(request, *args, **kwargs)
    
class AddPostItem(CreateView):
    model = Post
    fields = ['title', 'content', 'image']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class EditPostItem(UpdateView):
    model = Post
    fields = ['title', 'content', 'image']
    
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if not(self.request.user == obj.author or self.request.user.is_superuser):
            return HttpResponseForbidden()
        return super(EditPostItem, self).dispatch(request, *args, **kwargs)

class DeletePostItem(DeleteView):
    model = Post
    success_url = reverse_lazy('posts')
    
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if not(self.request.user == obj.author or self.request.user.is_superuser):
            return HttpResponseForbidden()
        return super(DeletePostItem, self).dispatch(request, *args, **kwargs)