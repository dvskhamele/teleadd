from django import template
from django.utils.safestring import mark_safe
register = template.Library()

@register.filter(name='current_status')
def current_status(status):
    status = str(status)
    if status=='UserStatusRecently()':
        return mark_safe("<span class='badge badge-success'>online</span>")
    else:
    	#UserStatusOffline(was_online=datetime.datetime(2019, 1, 2, 18, 58, 9, tzinfo=datetime.timezone.utc))
        s = s.split('datetime')
		s = s[2].split(', ')
		s = s[0]+"/"+s[1]+"/"+s[2]+")"
        return mark_safe("<span class='badge badge-dark'>offline since "+s+"</span>")
