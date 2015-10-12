from django.conf import settings
from councilmatic_core.models import Bill, Organization
from datetime import datetime
import pytz

app_timezone = pytz.timezone(settings.TIME_ZONE)

class NYCBill(Bill):

    class Meta:
        proxy = True

    def __str__(self):
        return self.friendly_name

    # the organization that's currently 'responsible' for a bill
    # this is usually whatever organization performed the most recent action, EXCEPT
    # for the case of bill referrals (when a bill is referred from city council to a committee), 
    # in which case it's the organization the bill was referred to
    @property
    def controlling_body(self):
        if self.current_action:
            related_orgs = self.current_action.related_entities.filter(entity_type='organization').all()
            if related_orgs:
                controlling_bodies = [Organization.objects.all().filter(ocd_id=org.organization_ocd_id).first() for org in related_orgs]
                return controlling_bodies
            else:
                return [self.current_action.organization]
        else:
            return None

    # whatever organization performed the most recent action
    @property
    def last_action_org(self):
        return self.current_action.organization if self.current_action else None

    # the most recent action on a bill
    @property
    def current_action(self):
        return self.actions.all().order_by('-order').first() if self.actions.all() else None

    # the date that a bill was passed, if it has been passed
    @property
    def date_passed(self):
        return self.actions.filter(classification='executive-signature').order_by('-order').first().date if self.actions.all() else None

    # NYC CUSTOMIZATION
    # makes a friendly name using bill type & number, e.g. 'Introduction 643-2015'
    # b/c this is how NYC peeps most often refer to a bill
    # this is what is used as the title (heading) for bills throughout the site (bill listing, bill detail)
    @property
    def friendly_name(self):
        nums_only = self.identifier.split(' ')[-1]
        return self.bill_type+' '+nums_only

    # the primary sponsorship for a bill
    @property
    def primary_sponsor(self):
        return self.sponsorships.filter(is_primary=True).first()

    # all committees that have been involved in the bill's history (the actions)
    # this is used to generate pseudo-topic tags for each bill in a listing
    @property
    def committees_involved(self):
        if self.actions.all():
            orgs = set([a.organization.name for a in self.actions.all() if (a.organization.name !='Mayor' and a.organization.name != 'New York City Council')])
            if not orgs and self.controlling_body and self.controlling_body[0].name != CITY_COUNCIL_NAME:
                orgs = self.controlling_body
            return list(orgs)
        else:
            return None

    # NYC CUSTOMIZATION
    # this is b/c we don't have data on bills voted against, only bills passed -
    # everything else is just left to die silently ¯\_(ツ)_/¯
    # turns out that ~80% of nyc bills that get passed, are passed within 
    # 2 months of the last action, so we're using that as a threshold for labeling bills as stale
    @property
    def is_stale(self):
        # stale = no action for 2 months
        if self.current_action:
            timediff = datetime.now().replace(tzinfo=app_timezone) - self.current_action.date
            return (timediff.days > 60)
        else:
            return True

    # NYC CUSTOMIZATION
    # whether or not a bill has reached its final 'completed' status
    # what the final status is depends on bill type
    @property
    def terminal_status(self):
        if self.actions:
            if self.bill_type == 'Introduction':
                if 'executive-signature' in [a.classification for a in self.actions.all()]:
                    return 'Passed'
                else:
                    return False
            elif self.bill_type in ['Resolution', 'Land Use Application', 'Communication', "Mayor's Message", 'Land Use Call-Up']: 
                if 'passage' in [a.classification for a in self.actions.all()]:
                    return 'Approved'
                else:
                    return False
        else:
            return False        

    # NYC CUSTOMIZATION
    # whether or not something has an approval among any of this actions
    # planning on using this for a progress bar for bills to lay out all the steps to law & how far it has gotten
    # (e.g. introduced -> approved by committee -> approved by council -> approved by mayor)
    @property
    def is_approved(self):
        if self.actions:
            return any(['Approved' in a.description for a in self.actions.all()])
        else:
            return False

    # NYC CUSTOMIZATION
    # the 'current status' of a bill, inferred with some custom logic
    # this is used in the colored label in bill listings
    @property
    def inferred_status(self):
        # these are the bill types for which a status doesn't make sense
        if self.bill_type in ['SLR', 'Petition', 'Local Laws 2015']:
            return None
        elif self.terminal_status:
            return self.terminal_status
        elif self.is_stale:
            return 'Stale'
        else:
            return 'Active'

    # date of most recent activity on a bill
    def get_last_action_date(self):
        return self.actions.all().order_by('-order').first().date if self.actions.all() else None

    # NYC CUSTOMIZATION
    # this is used for the text description of a bill in bill listings
    # the abstract is usually friendlier, so we want to use that whenever it's available,
    # & have the description as a fallback
    def listing_description(self):
        if self.abstract:
            return self.abstract
        else:
            return self.description
