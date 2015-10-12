from councilmatic_core.haystack_indexes import BillIndex
from haystack import indexes
from nyc.models import NYCBill

class NYCBillIndex(BillIndex, indexes.Indexable):
    
    def get_model(self):
        return NYCBill
