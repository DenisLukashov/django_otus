from django import template
from random import choice
from django.utils.safestring import mark_safe

register = template.Library()

jokes = ['1', '2', '3']


@register.simple_tag
def joke(index=None):
    if index is None or not isinstance(index, int) or index >= len(jokes):
        a_joke = choice(jokes)
    else:
        a_joke = jokes[index]
    return mark_safe(f'<p>{a_joke}</p>')
