# custom_filters.py
from django import template

from django.utils import timezone
from datetime import datetime, time

import markdown

register = template.Library()

@register.filter
def MD_to_HTML(value):
    return markdown.markdown(value, extensions=['markdown.extensions.tables', 'markdown.extensions.sane_lists'])


@register.filter
def is_date_greater_than_now(date):
    date_with_time = datetime.combine(date, time(hour=20))
    date_with_timezone = timezone.make_aware(date_with_time)
    return date_with_timezone > timezone.now()