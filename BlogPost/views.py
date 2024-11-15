from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from unicodedata import category

from .models import BlogPost, Category, Region


class PostListView(ListView):
    model = BlogPost
    template_name = 'home.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = BlogPost
    template_name = 'detail.html'


# def home(request):
#     first_news = BlogPost.objects.first()
#
#     three_news = BlogPost.objects.all()[1:4]
#
#     return render(request, 'home.html', {
#         'first_news': first_news,
#         'three_news': three_news,
#     })

def blogpost_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'home.html', {'posts': posts})

def blogpost_detail(request, pk):
    post = BlogPost.objects.get(pk=pk)
    return render(request, 'detail.html', {'post': post})

def detail(request, id):
    post = BlogPost.objects.get(id=id)
    category = Category.objects.get(id=post.category.id)
    rel_news = BlogPost.objects.filter(category=category).exclude(id=id)
    context = {'posts' : post,
               'category' : category,
               'rel_news' : rel_news
               }
    return render(request, 'detail.html', context)

def all_category(request):
    categories = Category.objects.all()
    return render(request , 'category.html' ,{
        'categories' : categories
    })


def category(request,id):
    category = Category.objects.get(id=id)
    posts = BlogPost.objects.filter(category=category)
    return render(request, 'category_detail.html', {'posts': posts, 'category': category})

def all_region(request) :
    regions = Region.objects.all()
    return render(request, 'region.html', {'regions': regions})

def region(request, id):
    region = Region.objects.get(id=id)
    posts = BlogPost.objects.filter(region=region)
    return render(request, 'region_detail.html', {'posts': posts,'region': region})


class Create_post(CreateView):
    model = BlogPost
    template_name = 'create-post.html'
    fields = ['category', 'region', 'title', 'text', 'image', 'author']


class Edit_post(UpdateView):
    model = BlogPost
    template_name = 'edit-post.html'
    fields = ['category', 'region', 'title', 'text']

class Delete_post(DeleteView):
    model = BlogPost
    template_name = 'delete-post.html'
    success_url = reverse_lazy('home')
