from django.urls import path

from .views import *
    
urlpatterns = [
    path('', ShowPostList.as_view(), name='posts'),
    path('add', AddPostItem.as_view(), name='add_post'),
    path('<pk>', ShowPostItem.as_view(), name='post'),
    path('<pk>/edit', EditPostItem.as_view(), name='edit_post'),
    path('<pk>/delete', DeletePostItem.as_view(), name='delete_post'),
]





