from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def sentence_case(value):
    return value.replace("_", " ").capitalize()