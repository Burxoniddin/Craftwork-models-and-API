from django.db import models
import datetime

from django.forms import DateField
from numpy import True_

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=256, verbose_name='name')
    content = models.TextField()
    image = models.ImageField(upload_to='post', null = True)
    
    author = models.ForeignKey( 'Author', on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, related_name='posts')
    
    published_date = models.DateTimeField(null = True)
    views_count = models.IntegerField(default=0)
    read_date = models.DateTimeField(auto_now_add = True)
    is_saved = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)
    
    
    
class Author(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    
    
    
class Category(models.Model):
    title = models.CharField(max_length = 100)
    
    
class Comment(models.Model):
    user = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='comment')
    content = models.TextField()
    comment_time = models.DateTimeField(auto_now_add = True_)