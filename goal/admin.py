from django.contrib import admin
from .models import Player, Goal, Match
from django import forms


admin.site.register(Player)
admin.site.register(Goal)
admin.site.register(Match)
