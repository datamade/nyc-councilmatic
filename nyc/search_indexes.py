from nyc.models import Bill
from haystack import indexes

class BillIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    slug = indexes.CharField(model_attr='slug', indexed=False)
    ocd_id = indexes.CharField(model_attr='ocd_id', indexed=False)
    bill_type = indexes.CharField(model_attr='bill_type', faceted=True)
    classification = indexes.CharField(model_attr='classification', faceted=True)
    identifier = indexes.CharField(model_attr='identifier')
    name = indexes.CharField(model_attr='name')
    date_created = indexes.DateTimeField(model_attr='date_created')
    date_updated = indexes.DateTimeField(model_attr='date_updated')
    sponsors = indexes.MultiValueField()
    source_url = indexes.CharField(model_attr='source_url', indexed=False)
    source_note = indexes.CharField(model_attr='source_note')

    from_organization = indexes.CharField(model_attr='from_organization', 
                                          faceted=True)

    from_organization_slug = indexes.CharField(indexed=False)

    def get_model(self):
        return Bill

    def prepare_sponsors(self, obj):
        return [person for person in obj.sponsorships.all()]
    
    def prepare_from_organization(self, obj):
        if obj.current_org:
            return obj.current_org.name

    def prepare_from_organization_slug(self, obj):
        if obj.current_org:
            return obj.current_org.slug
