from django.shortcuts import render
from django.views.generic.base import TemplateView

from .models import Post

# Create your views here.
class ShowAllPosts(TemplateView):
    template_name = "posts/posts_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog_posts'] = Post.objects.all()[:5]
        return context