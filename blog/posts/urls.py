from django.urls import path
from . import views
app_name = 'posts'

urlpatterns = [
    path("", views.posts_list, name="list"),   #the name="posts" is used when you use a named link like {% url 'posts'%} in a template file to refer to the view
    path("<slug:slug>", views.post_page, name="page"), #here, we have a path converter inside the <>. The left-side 'slug' is the path converter (it's a built-in keyword) and the right-side slug is the value for the slug (user-named) that we are passing to the post_page view
                                                        #check the posts_lists.html file to see how this is referred
]
