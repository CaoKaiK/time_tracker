from django import template

from datetime import time

register = template.Library()

@register.filter('hour_minute_format')
def hour_minute_format(value):
   
    value = int(value)

    hours = int(value/60)
    minutes = value%60


    return '%s:%02d' % (hours,minutes)