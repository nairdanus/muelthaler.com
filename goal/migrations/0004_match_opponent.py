# Generated by Django 5.0.4 on 2024-05-09 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goal', '0003_remove_goal_scored_at_goal_goals_scored_match_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='opponent',
            field=models.CharField(default='Unbekannter Gegner', max_length=100),
        ),
    ]
