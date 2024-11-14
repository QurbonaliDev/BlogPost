from django.template.context_processors import static
from django.urls import path

from config import settings
from . import views
from .views import category, all_category, region, all_region

urlpatterns = [
    path('', views.blogpost_list, name='home'),
    path('<int:pk>/', views.blogpost_detail, name='detail'),
    path('category/<int:id>',category, name='category'),
    path('all_category',all_category, name='all_category'),
    path('region/<int:id>',region, name='region'),
    path('all_region',all_region, name='all_region'),
]

