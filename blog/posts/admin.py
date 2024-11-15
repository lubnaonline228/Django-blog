from django.contrib import admin
from .models import Post

# Register your models here.
# if we create any models and want to see them in the admin panel, we need to first register them here
admin.site.register(Post)  #this will create a model based on the class Post
