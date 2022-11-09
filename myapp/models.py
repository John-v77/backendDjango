from django.db import models
from datetime import datetime

# Create your models here.

    # Model for Index page
class Feature(models.Model):
    name=models.CharField(max_length=100)
    details=models.CharField(max_length=200)

    # Model for blogs
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000000)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    
    # Models for Chat App
class Room(models.Model):
    name = models.CharField(max_length=1000)

 
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000)
    room = models.CharField(max_length=1000)
    