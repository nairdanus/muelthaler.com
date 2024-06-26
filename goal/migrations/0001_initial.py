# Generated by Django 5.0.6 on 2024-05-10 11:46

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opponent', models.CharField(default='Unbekannter Gegner', max_length=100)),
                ('report', models.TextField(blank=True, default='')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('counter_goals', models.PositiveIntegerField(default=0)),
                ('group_picture', models.ImageField(blank=True, null=True, upload_to='group_pictures/')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pictures/')),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goals_scored', models.PositiveIntegerField(default=0)),
                ('match', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='goal.match')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goal.player')),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='players',
            field=models.ManyToManyField(related_name='matches', through='goal.Goal', to='goal.player'),
        ),
    ]
