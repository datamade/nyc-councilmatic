from councilmatic_core.haystack_indexes import BillIndex
from haystack import indexes
from nyc.models import NYCBill

class NYCBillIndex(BillIndex, indexes.Indexable):
    
    def get_model(self):
        return NYCBill

    def index_queryset(self, using=None):
        # excluding NYC bill types that are not really legislation
        invalid_bill_types = ['Town Hall Meeting', 'Oversight', 'Tour', 'Local Laws 2015']
        return self.get_model().objects.exclude(bill_type__in=invalid_bill_types)
