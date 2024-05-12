# custom_filters.py
from django import template

from django.utils import timezone
from datetime import datetime, time

import markdown

register = template.Library()

@register.filter
def markdown_to_html(markdown_text):
    html = markdown.markdown(markdown_text, extensions=['markdown.extensions.tables', 'markdown.extensions.sane_lists'])
    return html


@register.filter
def is_date_greater_than_now(date):
    date_with_time = datetime.combine(date, time(hour=20))
    date_with_timezone = timezone.make_aware(date_with_time)
    return date_with_timezone > timezone.now()