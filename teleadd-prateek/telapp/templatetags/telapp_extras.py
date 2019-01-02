from django import template
from django.utils.safestring import mark_safe
register = template.Library()

@register.filter(name='current_time')
def current_time(status):
    status = str(status)
    if status=='UserStatusRecently()':
        return mark_safe("<span class='badge badge-success'>online</span>")
    else:
        #sf = status.split('UserStatusOffline(was_online=datetime.datetime(')
        return mark_safe("<span class='badge badge-dark'>ofline</span>")
