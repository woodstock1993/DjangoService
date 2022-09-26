from tkinter import CASCADE
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author_id')
    title = models.CharField(max_length=200, default="")
    text = models.TextField(default= "")
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Tweet(models.Model):
    tweet = models.TextField(blank=True)
    favorite = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='user_favorite')

    def __unicode__(self):
        return self.tweet;


class User(AbstractUser):
    tweet = models.ManyToManyField(Tweet)
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)


class Amodel(models.Model):
    a = models.CharField(max_length=128, blank=True)
    b = models.CharField(max_length=128, blank=True)
    c = models.CharField(max_length=128, blank=True)

class Bmodel(models.Model):
    a = models.CharField(max_length=128, blank=True)
    b = models.CharField(max_length=128, blank=True)
    d = models.CharField(max_length=128, blank=True)
