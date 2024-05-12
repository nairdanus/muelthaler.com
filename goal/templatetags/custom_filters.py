# custom_filters.py
from django import template

from django.utils import timezone
from datetime import datetime

import markdown

register = template.Library()

@register.filter
def markdown_to_html(markdown_text):
    return markdown.markdown(markdown_text, extensions=['markdown.extensions.tables'])

@register.filter
def is_date_greater_than_now(date):
    # Convert date to datetime and make it aware of timezone
    date_with_timezone = timezone.make_aware(datetime.combine(date, datetime.min.time()))
    return date_with_timezone > timezone.now()