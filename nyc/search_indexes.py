from nyc.models import Bill
from haystack import indexes
import re

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

    actions = indexes.MultiValueField()

    from_organization = indexes.CharField(model_attr='from_organization', 
                                          faceted=True)

    from_organization_slug = indexes.CharField(indexed=False)

    def get_model(self):
        return Bill

    def prepare_friendly_name(self, obj):
        return obj.friendly_name

    def prepare_sponsorships(self, obj):
        return [sponsorship.person for sponsorship in obj.sponsorships.all()]

    def prepare_actions(self, obj):
        return [action for action in obj.actions.all()]
    
    def prepare_from_organization(self, obj):
        if obj.current_org:
            return obj.current_org.name

    def prepare_from_organization_slug(self, obj):
        if obj.current_org:
            return obj.current_org.slug

    def prepare_full_text(self, obj):
        return re.sub(r'<[^>]*?>', ' ', obj.full_text)
