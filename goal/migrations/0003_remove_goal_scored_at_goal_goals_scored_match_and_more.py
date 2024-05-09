# Generated by Django 5.0.4 on 2024-05-09 00:05

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goal', '0002_player_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goal',
            name='scored_at',
        ),
        migrations.AddField(
            model_name='goal',
            name='goals_scored',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('counter_goals', models.PositiveIntegerField(default=0)),
                ('group_picture', models.ImageField(blank=True, null=True, upload_to='group_pictures/')),
                ('players', models.ManyToManyField(related_name='matches', through='goal.Goal', to='goal.player')),
            ],
        ),
        migrations.AddField(
            model_name='goal',
            name='match',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='goal.match'),
        ),
    ]
