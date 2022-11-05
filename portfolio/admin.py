from django.contrib import admin
from portfolio.models import Choice, Poll, Vote

# Polls On Admin Side
admin.site.register(Choice)
admin.site.register(Poll)
admin.site.register(Vote)

