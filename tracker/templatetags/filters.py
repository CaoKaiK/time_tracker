from django import template

from datetime import time

register = template.Library()

@register.filter('hour_minute_format')
def hour_minute_format(value):
   
    value = int(value)
    hours = int(value/60)
    minutes = value%60
    return '%s:%02d' % (hours,minutes)

@register.filter('duration')
def duration(td):
    total_seconds = int(td.total_seconds())
    if total_seconds < 0:
        total_seconds = abs(total_seconds)
        hours = -total_seconds // 3600 +1
        minutes = (total_seconds % 3600) // 60
    else:
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
    return '%02d:%02d' % (hours,minutes)
