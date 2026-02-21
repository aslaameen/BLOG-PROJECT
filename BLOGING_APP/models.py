from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.




class Login(AbstractUser):
    is_blogger = models.BooleanField(default=False)

class Blogger(models.Model):
    blogger_details = models.OneToOneField("Login", on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    bio = models.TextField(max_length=500)
    document = models.FileField(upload_to='documents/')

class BlogPost(models.Model):
    blog_details = models.ForeignKey("Blogger", on_delete=models.CASCADE)
    title = models.CharField()
    content = models.TextField()
    document = models.FileField(upload_to='documents/')
    date = models.DateField()