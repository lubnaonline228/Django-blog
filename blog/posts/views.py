from django.shortcuts import render
from .models import Post

# Create your views here.

def posts_list(request):
    posts=Post.objects.all().order_by('-date')  #when you add '-' sign before date, it orders the posts by date in descending order. So the latest blog is shown first
    return render(request, 'posts/posts_list.html', {'posts': posts})  # this passes a python dictionary with all my Post objects as data to the posts_list.html template

def post_page(request, slug):
    post=Post.objects.get(slug=slug)   #this will get only the post object where the slug field (that's on the left side of the '=') contains the value in slug (that's on the right side of the '='). The right side slug is obtained from the slug value passed to this function (post_page) in line 10
    return render(request, 'posts/post_page.html', {'post': post})  
