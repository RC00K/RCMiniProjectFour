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


class Review(models.Model):
    user = models.ForeignKey(User, related_name="reviews", on_delete=models.DO_NOTHING)

    title = models.CharField(max_length=50)
    body = models.CharField(max_length=150)

    def __str__(self):
        return (
            f"{self.user} "
            f"{self.title[:30]}..."
            f"{self.body[:30]}..."
        )
