from django.urls import path

from .views import *
    
urlpatterns = [
    path('', ShowAllPosts.as_view(), name='posts'),
    path('<int:pk>', ShowPost.as_view(), name='post'),
]




