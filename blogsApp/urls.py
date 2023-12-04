from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get-all-posts', views.getAllPosts, name='get-all-posts'),
    path('get-post/<int:id>', views.getPost, name='get-post'),
    path('create-new-post', views.createPost, name='create-new-post'),
    path('update-post/<int:id>', views.updatePost, name='update-post'),
    path('delete-post/<int:id>', views.deletePost, name='delete-post'),
]
