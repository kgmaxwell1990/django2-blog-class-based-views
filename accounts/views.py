from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

class LoginView(SuccessMessageMixin, LoginView):
    template_name = 'accounts/login.html'
    form_class = AuthenticationForm
    success_message = "You have been logged in"

class LogoutView(LogoutView):
    next_page = "/"
    
class ProfileView(TemplateView):
    template_name = "accounts/profile.html"
    
class RegistrationView(SuccessMessageMixin, CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('profile')
    template_name = 'accounts/register.html'
    success_message = "Thank you for registering!"

    def form_valid(self, form):
        valid = super(RegistrationView, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid
    
    