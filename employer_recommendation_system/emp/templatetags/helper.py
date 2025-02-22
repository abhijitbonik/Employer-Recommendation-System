from django import template
from django.conf import settings

register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name):
    group_list = []
    for item in user.groups.all():
        group_list.append(item.name)
    return True if group_name in group_list else False

