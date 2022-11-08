import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Choice(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Poll(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    choices = models.ManyToManyField(
        Choice, related_name='related_polls', blank=True)

    def __str__(self):
        return self.name


class Vote(models.Model):
    poll = models.ForeignKey(
        Poll, on_delete=models.SET_NULL, related_name="votes", null=True, blank=True)
    choice = models.ForeignKey(
        Choice, on_delete=models.SET_NULL, related_name="votes", null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.poll.name} - {self.choice.name}"


class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author:}: {self.title}'

    def get_absolute_url(self):
        return reverse("review", kwargs={'pk': self.pk})
