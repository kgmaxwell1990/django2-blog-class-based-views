from django.shortcuts import render
from django.views.generic.base import TemplateView

def error_404_view(request, exception):
    return render(request,'home/error_404.html')

class HomePageView(TemplateView):
    template_name = "home/index.html"


    
