# custom_filters.py
from django import template

from django.utils import timezone
from datetime import datetime, time

import markdown

register = template.Library()


def custom_MD_controls(value):
    value = value.replace("+hl+", "---")
    value = value.replace("+table+", "<table>").replace("+/table+", "</table>")
    value = value.replace("+tr+", "<tr>").replace("+/tr+", "</tr>")
    value = value.replace("+th+", "<th>").replace("+/th+", "</th>")
    value = value.replace("+td+", "<td>").replace("+/td+", "</td>")
    return value


@register.filter
def MD_to_HTML(value):
    return markdown.markdown(custom_MD_controls(value), 
        extensions=['markdown.extensions.tables', 'markdown.extensions.sane_lists'])


@register.filter
def is_date_greater_than_now(date):
    date_with_time = datetime.combine(date, time(hour=20))
    date_with_timezone = timezone.make_aware(date_with_time)
    return date_with_timezone > timezone.now()