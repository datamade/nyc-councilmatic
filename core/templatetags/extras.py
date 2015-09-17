from django import template
from django.template.defaultfilters import stringfilter
from django.utils.html import strip_entities, strip_tags
import re

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
    if value == 'controlling_body': return 'Controlling body'

@register.filter
@stringfilter
def remove_action_subj(bill_action_desc):
	# removes 'by X' from bill action descriptions & expands abbrevs
	# for more readable action labels
	clean_action = re.sub(r'\bComm\b', 'Committee', bill_action_desc)
	clean_action = re.sub(r'\bRecved\b', 'Received', clean_action)
	clean_action = re.sub(r'[,\s]*by\s[^\s]*', '', clean_action)

	# shorten the really long action descriptions for approval w/ modifications
	if 'approved with modifications' in clean_action.lower():
		clean_action = 'Approved with Modifications'

	return clean_action

@register.filter
@stringfilter
def short_blurb(text_blob):
	if len(text_blob) > 200:
		blurb = text_blob[:200]
		blurb = blurb[:blurb.rfind(' ')]+' ...'
		return blurb
	else:
		return text_blob

@register.filter
@stringfilter
def strip_mailto(email):
	return re.sub('mailto:', '', email)

@register.filter
@stringfilter
def clean_html(text):
    return strip_entities(strip_tags(text)).replace('\n','')

@register.filter
@stringfilter
def alternative_identifiers(id_original):
    id_1 = re.sub(" ", " 0", id_original)
    id_2 = re.sub(" ", "", id_original)
    id_3 = re.sub(" ", "", id_1)
    return id_original+' '+id_1+' '+id_2+' '+id_3