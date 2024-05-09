from django.contrib import admin
from .models import Player, Goal, Match

admin.site.register(Player)
admin.site.register(Goal)
admin.site.register(Match)