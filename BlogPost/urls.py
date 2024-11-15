from django.template.context_processors import static
from django.urls import path

from config import settings
from . import views
from .views import category, all_category, region, all_region, Create_post, Edit_post, Delete_post

urlpatterns = [
    path('', views.blogpost_list, name='home'),
    path('detail/<int:pk>/', views.blogpost_detail, name='detail'),
    path('category/<int:id>',category, name='category'),
    path('all_category',all_category, name='all_category'),
    path('region/<int:id>',region, name='region'),
    path('all_region',all_region, name='all_region'),
    path('create-post/new', Create_post.as_view(), name='create_post'),
    path('edit-post/<int:pk>', Edit_post.as_view(), name='edit_post'),
    path('delete-post/<int:pk>', Delete_post.as_view(), name='delete_post'),
]

