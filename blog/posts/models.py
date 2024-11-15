from django.db import models

# Create your models here.
# Migrations take your python code (the classes or models) and turns them into a database tables

class Post(models.Model):  # Here the class "Post" is inheriting the models.Model class. In other words, "Post" is basically a Model, with its own attributes
    title=models.CharField(max_length=75)  #Here Title is using the 'Charfield' attribute from the 'models' class that was imported in line 1
    body = models.TextField()
    slug = models.SlugField()    # A slug is part of the url used to identify the post. For example /nahid-post
    date= models.DateTimeField(auto_now_add=True)     #This refers to the date when the post was created

    def __str__(self):
        return self.title

