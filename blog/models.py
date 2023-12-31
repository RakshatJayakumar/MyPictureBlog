# blog/models.py
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self):
        return self.title