# Generated by Django 5.0.6 on 2024-05-13 13:55

import goal.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goal', '0002_match_pre_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='pre_report',
            field=goal.models.MarkdownHTMLField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='match',
            name='report',
            field=goal.models.MarkdownHTMLField(blank=True, default=''),
        ),
    ]