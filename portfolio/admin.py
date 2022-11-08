from django.contrib import admin
from portfolio.models import Choice, Poll, Vote, Post

# Polls On Admin Side
admin.site.register(Choice)
admin.site.register(Poll)
admin.site.register(Vote)
admin.site.register(Post)

