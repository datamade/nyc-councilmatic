from councilmatic_core.feeds import CouncilmaticFacetedSearchFeed, BillDetailActionFeed
from nyc.models import NYCBill

class NYCCouncilmaticFacetedSearchFeed(CouncilmaticFacetedSearchFeed):
    # same as CouncilmaticFacetedSearchFeed but have a better item name template which uses
    # NYCBill's friendly_name() as opposed to Bill's friendly_name()
    title_template = 'feeds/nyc_search_item_title.html'
    bill_model = NYCBill
    
class NYCBillDetailActionFeed(BillDetailActionFeed):
    title_template = 'feeds/nyc_bill_actions_item_title.html'
    
