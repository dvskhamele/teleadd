from django import template
from django.utils.safestring import mark_safe
register = template.Library()

@register.filter(name='current_status')
def current_status(status):
    try:
        status = status.was_online
        return mark_safe("<span class='badge badge-dark'>offline since "+str(status)+"</span>")
    except:
    	return mark_safe("<span class='badge badge-success'>online</span>")