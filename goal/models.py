from django.db import models
from django.utils import timezone

from django.utils.html import mark_safe


class MarkdownHTMLField(models.TextField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self, value, model_instance):
        value = super().clean(value, model_instance)
        return mark_safe(html_content)


class Player(models.Model):
    name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.name

class Match(models.Model):
    opponent = models.CharField(max_length=100, default="Unbekannter Gegner")
    pre_report = MarkdownHTMLField(default="", blank=True)
    report = MarkdownHTMLField(default="", blank=True)
    date = models.DateField(default=timezone.now)
    players = models.ManyToManyField(Player, through='Goal', related_name='matches')
    counter_goals = models.PositiveIntegerField(default=0)
    group_picture = models.ImageField(upload_to='group_pictures/', blank=True, null=True)

    def __str__(self):
        return self.opponent
    

class Goal(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, default=None)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    goals_scored = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.player.name} - {self.match.date} - {self.goals_scored} goals"
