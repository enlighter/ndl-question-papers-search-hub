from django import template

register = template.Library()

@register.filter
def erange(value):
    return range(value)