from nyc.models import Bill
from haystack import indexes
from nyc.templatetags.nyc_extras import clean_html

class BillIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    slug = indexes.CharField(model_attr='slug', indexed=False)
    ocd_id = indexes.CharField(model_attr='ocd_id', indexed=False)
    bill_type = indexes.CharField(model_attr='bill_type', faceted=True)
    classification = indexes.CharField(model_attr='classification')
    identifier = indexes.CharField(model_attr='identifier')
    description = indexes.CharField(model_attr='description')
    friendly_name = indexes.CharField()
    sponsorships = indexes.MultiValueField(faceted=True)
    source_url = indexes.CharField(model_attr='source_url', indexed=False)
    source_note = indexes.CharField(model_attr='source_note')
    full_text = indexes.CharField(model_attr='full_text')
    last_action_date = indexes.DateTimeField()

    actions = indexes.MultiValueField()

    controlling_body = indexes.MultiValueField(faceted=True)

    def get_model(self):
        return Bill

    def prepare_friendly_name(self, obj):
        return obj.friendly_name

    def prepare_sponsorships(self, obj):
        return [sponsorship.person.name for sponsorship in obj.sponsorships.all()]

    def prepare_actions(self, obj):
        return [action for action in obj.actions.all()]
    
    def prepare_controlling_body(self, obj):
        if obj.controlling_body:
            return [org.name for org in obj.controlling_body]

    def prepare_full_text(self, obj):
        return clean_html(obj.full_text)
    
    def prepare_last_action_date(self, obj):
        from datetime import datetime, timedelta
        if not obj.last_action_date:
            return datetime.now() - timedelta(days=36500)
        return obj.last_action_date
