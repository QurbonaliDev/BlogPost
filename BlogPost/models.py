from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE, blank=True, null= True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE,blank=True ,null= True)
    title = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
