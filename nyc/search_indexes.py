
from haystack import indexes

from django.conf import settings

from datetime import datetime, timedelta
import pytz

from nyc.models import NYCBill
from councilmatic_core.haystack_indexes import BillIndex
from councilmatic_core.models import Action


class NYCBillIndex(BillIndex, indexes.Indexable):

    def get_model(self):
        return NYCBill

    def index_queryset(self, using=None):
        # excluding NYC bill types that are not really legislation
        invalid_bill_types = ['Town Hall Meeting', 'Oversight', 'Tour', 'Local Laws 2015']
        return self.get_model().objects.exclude(bill_type__in=invalid_bill_types)

    def prepare_last_action_date(self, obj):

        if not obj.last_action_date:
            index_actions = [a.date for a in obj.actions.all()]

            if index_actions:
            
                return max(index_actions).strftime('%Y-%m-%dT%H:%M:%SZ')
            
            return index_actions

        return obj.last_action_date.strftime('%Y-%m-%dT%H:%M:%SZ')
