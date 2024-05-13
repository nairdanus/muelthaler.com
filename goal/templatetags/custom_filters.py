# custom_filters.py
from django import template

from django.utils import timezone
from datetime import datetime, time


register = template.Library()



@register.filter
def is_date_greater_than_now(date):
    date_with_time = datetime.combine(date, time(hour=20))
    date_with_timezone = timezone.make_aware(date_with_time)
    return date_with_timezone > timezone.now()