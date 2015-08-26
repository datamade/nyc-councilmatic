from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def sentence_case(value):
    return value.replace("_", " ").capitalize()

@register.filter
@stringfilter
def facet_name(value):
    if value == 'bill_type': 
        value = 'Legislation type'
    elif value == 'sponsorships': 
        value = 'Sponsor'
    elif value == 'from_organization': 
        value = 'Legislative body'
    return value
