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
    if value == 'bill_type': return 'Legislation type'
    if value == 'sponsorships': return 'Sponsor'
    if value == 'from_organization': return 'Legislative body'
