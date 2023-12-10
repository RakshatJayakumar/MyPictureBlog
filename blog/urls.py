# blog/urls.py
from django.urls import path
from .views import post_list, post_new, post_detail, post_edit, post_delete

urlpatterns = [
    path('post/', post_list, name='post_list'),
    path('post/new/', post_new, name='post_new'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', post_delete, name='post_delete'),
]