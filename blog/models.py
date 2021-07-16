from django.db import models

# Create your models here.

class Test(models.Model):
    name = models.CharField(max_length=254)



'''class BlogPosts(models.Model):
    date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    content = models.TextField()
    category = models.CharField(max_length=100)


class Projects(models.Model):
    date = models.CharField(max_length=100)
    project_name = models.CharField(max_length=254)
    description = models.TextField()'''
    #filefield right here to insert a cool preview pic of the project


