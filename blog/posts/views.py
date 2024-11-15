from django.shortcuts import render
from .models import Post

# Create your views here.

def posts_list(request):
    posts=Post.objects.all().order_by('-date')  #when you add '-' sign before date, it orders the posts by date in descending order. So the latest blog is shown first
    return render(request, 'posts/posts_list.html', {'posts': posts})  # this passes a python dictionary with all my Post objects as data to the posts_list.html template

