# These are all the settings specific to a city

CITY_NAME = 'New York City'


OCD_JURISDICTION_ID = 'ocd-jurisdiction/country:us/state:ny/place:new_york/government'
OCD_CITY_COUNCIL_ID = 'ocd-organization/389257d3-aefe-42df-b3a2-a0d56d0ea731'


TIMEZONE = 'US/Eastern'


LEGISLATION_TYPE_DESCRIPTIONS = [
	{
		'name': 'Introduction',
		'search_term': 'Introduction',
		'desc': 'A proposal for a NYC local law. \
				An introduction becomes a local law if (1) both the Council & Mayor approve, \
				(2) the Mayor vetoes but the Council achieves 2/3 vote within 30 days of the veto, or\
				(3) the Council approves and the mayor does not act within 30 days.',

	},
	{
		'name': 'Resolution',
		'search_term': 'Resolution',
		'desc': "An expression of the Council's sentiment on important public policy issues that may or may not fall under City jurisdiction. \
				Resolutions are often used to support federal or state legislation, commemorate people and events, or even criticize policies. \
				Resolutions can also be used to adopt budget and land use items.",
	},
	{
		'name': 'SLR (State Legislation Resolution)',
		'search_term': 'SLR',
		'desc': 'A special resolution that serves as an official home rule request from the Council to the State Senate and State Assembly to pass pending legislation in the New York State Legislature. The initial request for a SLR must come from the Legislature in Albany.',
	},
	{
		'name': 'Oversight',
		'search_term': 'Oversight',
		'desc': 'A hearing held with respect to an oversight topic not on a specific piece of legislation.',
	},
	{
		'name': 'Land Use Application',
		'search_term': 'Land Use Application',
		'desc': 'Land use proposals to be considered by the Council’s Land Use Committee',
	},
	{
		'name': 'Land Use Call-Up',
		'search_term': 'Land Use Call-Up',
		'desc': "Land use proposals that don't require Council approval, but have been chosen by a Council Member for discretionary Council review.",
	},
	{
		'name': 'Tour',
		'search_term': 'Tour',
		'desc': 'A site visit taken by members of a committee, for fact-finding relevant to the committee’s decision-making. A tour is considered an official committee meeting.',
	},
	{
		'name': 'Local Law 2015',
		'search_term': 'Local Laws 2015',
		'desc': 'All NYC laws that have been enacted for the year 2015.',
	},
	{
		'name': 'Mayor’s Messages',
		'search_term': "Mayor's Message",
		'desc': 'Communications from the Mayor. These generally include appointments to boards and commissions, as well as veto messages.',
	},
	{
		'name': 'Communications',
		'search_term': 'Communication',
		'desc': 'Communications from the City, County or Borough offices. These usually concern appointments to boards and commissions.',
	},
	{
		'name': 'Petitions',
		'search_term': 'Petition',
		'desc': 'Communication from individuals or entities other than the Mayor, City, County or Borough Offices. These generally include communications from the City Council, and usually concern City Council appointments and resignations.',
	},
]