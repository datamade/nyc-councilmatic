# These are all the settings specific to a city

CITY_NAME = 'New York City'


OCD_JURISDICTION_ID = 'ocd-jurisdiction/country:us/state:ny/place:new_york/government'
OCD_CITY_COUNCIL_ID = 'ocd-organization/389257d3-aefe-42df-b3a2-a0d56d0ea731'


TIMEZONE = 'US/Eastern'


LEGISLATION_TYPE_DESCRIPTIONS = [
	{
		'name': 'Introduction',
		'search_term': 'Introduction',
		'desc': 'Council makes and passes the laws governing the city. Legislation pending in the Council is called an Introduction. When an Introduction is passed by the Council and adopted in one of the 3 ways described below it becomes a Local Law and is given a Local Law number.\n\
				Once the Introduction is approved by the Council it is sent to the Mayor who holds a public hearing on it. Once it is signed by the Mayor it becomes a Local Law.\n\
				If the Mayor disapproves and vetoes the Introduction, the bill comes back to the Council with the Mayor’s written objections (Veto Message). The Council at a subsequent meeting held within 30 days can override the Mayor’s veto by a two-thirds vote.\n\
				If the Mayor chooses not to sign or veto a bill within a prescribed thirty-day time period, the introduction becomes a local law and is enacted pursuant to the City Charter due to the lack of Mayoral action.',

	},
	{
		'name': 'Resolution',
		'search_term': 'Resolution',
		'desc': 'Resolutions are used by the Council as a vehicle for legislative action and to express the sentiment of the body on important public policy issues. These issues may or may not fall under City jurisdiction. Resolutions are often used to support federal or state legislation, commemorate people and historical dates, or even criticize or denounce practices and policies. Resolutions are also mechanisms in which the Council adopts the budget and land use items.',
	},
	{
		'name': 'Oversight',
		'search_term': 'Oversight',
		'desc': 'A hearing held with respect to an oversight topic not on a specific piece of legislation.',
	},
	{
		'name': 'Land Use Application',
		'search_term': 'Land Use Application',
		'desc': 'Each application or submission that is to be considered by the Council’s Land Use Committee',
	},
	{
		'name': 'Communications',
		'search_term': 'Communication',
		'desc': 'Communications sent by city, county and borough offices to the Council for consideration. These include requests for advice and consent on appointments to various boards and commissions.',
	},
	{
		'name': 'Land Use Call-Up',
		'search_term': 'Land Use Call-Up',
		'desc': 'Land use items that do not require Council approval to be enacted but have been chosen by any given Council Member for discretionary review by the Council.',
	},
	{
		'name': 'Mayor’s Messages',
		'search_term': "Mayor's Message",
		'desc': 'Messages and Papers from the Mayor include Mayoral Home Rules Requests, requests for advice and consent on appointments to various City commissions and boards, and veto messages.',
	},
	{
		'name': 'SLR (State Legislation Resolution)',
		'search_term': 'SLR',
		'desc': 'A special resolution that serves as an official home rule request from the Council to the State Senate and State Assembly to pass pending legislation in the New York State Legislature. The initial request for a SLR must come from the Legislature in Albany.',
	},
	{
		'name': 'Tour',
		'search_term': 'Tour',
		'desc': 'A brief fact-finding trip taken by members of a respective committee in order to view or inspect a place or site that has relevance to their committee’s jurisdiction. It is considered an official meeting of a Committee.',
	},
	{
		'name': 'Local Law 2015',
		'search_term': 'Local Laws 2015',
		'desc': 'All local laws that have been enacted for the year 2015.',
	},
	{
		'name': 'Petitions/Communications',
		'search_term': 'Communication',
		'desc': 'Communication originating from individuals or entities other than the Mayor, City, County and Borough Offices. These generally include communications from the Council, such as Council appointments and resignations.',
	},
]