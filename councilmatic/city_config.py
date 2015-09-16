# These are all the settings specific to a city

CITY_NAME = 'New York City'
CITY_COUNCIL_NAME = 'New York City Council'


OCD_JURISDICTION_ID = 'ocd-jurisdiction/country:us/state:ny/place:new_york/government'
OCD_CITY_COUNCIL_ID = 'ocd-organization/389257d3-aefe-42df-b3a2-a0d56d0ea731'


TIMEZONE = 'US/Eastern'


SEARCH_PLACEHOLDER_TEXT = "Taxi, Resolution 815-2015, Land Use Application, etc."



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

# these keys should match committee slugs
COMMITTEE_DESCIPTIONS = {
	"committee-on-aging" : 					"Department for the Aging and all federal, state and municipal programs pertinent to senior citizens",
	"committee-on-civil-rights" : 			"Human Rights Commission, Equal Employment Practices Commission and Equal Employment Opportunity",
	"committee-on-civil-service-and-labor" : "Municipal Officers and Employees, Office of Labor Relations, Office of Collective Bargaining, Office of Labor Services, and Municipal Pension and Retirement Systems",
	"committee-on-community-development" : 	"Issues relating to poverty and its reduction especially in low income neighborhoods",
	"committee-on-consumer-affairs" : 		"Department of Consumer Affairs",
	"committee-on-contracts" : 				"Procurement Policy Board, review of City procurement policies and procedures, oversight over government contracts, Mayor's Office of Contract Services and collection agency contracts",
	"committee-on-courts-and-legal-services" : "Courts and Legal Aid",
	"committee-on-cultural-affairs-libraries-and-international-intergroup-relations" : "Department of Cultural Affairs, libraries, museums, Art Commission, New York City Commission for the United Nations, Consular Corps and Protocol, Mayor’s Office of Special Projects and Community Events, and to encourage harmony among the citizens of New York City, to promote the image of New York City and enhance the relationship of its citizens with the international community",
	"committee-on-economic-development" : 	"Economic Development Corporation and Department of Small Business Services",
	"committee-on-education" : 				"Department of Education, School Construction Authority and charter schools",
	"committee-on-environmental-protection" : "Department of Environmental Protection and Office of Long Term Planning and Sustainability",
	"committee-on-finance" : 				"Executive Budget review and Budget modification, Banking Commission, Comptroller's Office, Department of Design and Construction, Department of Finance, Independent Budget Office and fiscal policy and revenue from any source",
	"committee-on-fire-and-criminal-justice-services" : "Fire/EMS (non-health related issues), Department of Probation, Department of Correction, and Emergency Management Department (OEM)",
	"committee-on-general-welfare" : 		"Human Resources Administration/Department of Social Services, Administration for Children's Services, Department of Homeless Services, Office of Immigrant Affairs and charitable institutions",
	"committee-on-governmental-operations" : "Municipal governmental structure and organization, Department of Citywide Administrative Services, Community Boards, Tax Commission, Board of Standards and Appeals, Campaign Finance Board, Board of Elections, Voter Assistance Commission, Commission on Public Information and Communication, Department of Records and Information Services, Financial Information Services Agency and Law Department",
	"committee-on-health" : 				"Department of Health and Mental Hygiene, Health and Hospitals Corporation and Office of the Chief Medical Examiner and EMS (health related issues)",
	"committee-on-higher-education" : 		"City University of New York",
	"committee-on-housing-and-buildings" : 	"Department of Housing Preservation and Development, Department of Buildings and rent regulation",
	"committee-on-immigration" : 			"Mayor’s Office of Immigrant Affairs and other matters affecting immigration",
	"committee-on-juvenile-justice" : 		"Division of Youth and Family Justice within the Administration for Children’s Services",
	"committee-on-land-use" : 				"City Planning Commission, Department of City Planning, Department of Information Technology and Telecommunications, Landmarks Preservation Commission, land use and landmarks review",
	"committee-on-mental-health-developmental-disability-alcoholism-drug-abuse-and-disability-services" : "Department of Health and Mental Hygiene (issues of mental health, developmental disability and alcoholism services) and Mayor’s Office for People with Disabilities",
	"committee-on-mental-health-developmental-disability-alcoholism-substance-abuse-and-disability-services" : "Department of Health and Mental Hygiene (issues of mental health, developmental disability and alcoholism services) and Mayor’s Office for People with Disabilities",
	"committee-on-oversight-and-investigations" : "To investigate any matters within the jurisdiction of the Council relating to property, affairs, or government of New York City and the Department of Investigation",
	"committee-on-parks-and-recreation" : 	"Department of Parks and Recreation",
	"committee-on-public-housing" : 		"NYC Housing Authority",
	"committee-on-public-safety" : 			"Police Department, District Attorneys, Special Narcotics Prosecutor, Civilian Complaint Review Board, and Criminal Justice Coordinator",
	"committee-on-recovery-and-resiliency" : "Office of Recovery and Resiliency, issues relating to recovery in Hurricane Sandy affected communities, including the Build It Back Program, and the Office of Long Term Planning and Sustainability as it relates to efforts to make New York City more resilient in the face of climate change, and preparing for, responding to, and recovering from emergencies",
	"committee-on-rules-privileges-and-elections" : "Council structure and organization and appointments",
	"committee-on-sanitation-and-solid-waste-management" : "Department of Sanitation and the Business Integrity Commission",
	"committee-on-small-business" : 		"Matters relating to retail business and emerging industries",
	"committee-on-standards-and-ethics" : 	"Conflicts of Interest Board and Council Ethics",
	"committee-on-state-and-federal-legislation" : "Federal legislation, State legislation and Home Rule requests",
	"committee-on-technology":				"Technology in New York City, Department of Information Technology and Telecommunications (non-land use-related issues), Mayor’s Office of Media & Entertainment, NYC TV and dissemination of public information through the use of technology",
	"committee-on-transportation" : 		"Mass Transportation Agencies and facilities, Department of Transportation, New York City Transit Authority and Taxi and Limousine Commission",
	"committee-on-veterans" : 				"Mayor’s Office of Veterans Affairs and other veteran related issues",
	"committee-on-waterfronts" : 			"Matters relating to the waterfront",
	"committee-on-womens-issues" : 		"Issues relating to public policy concerns of women, domestic violence, Office to Combat Domestic Violence and Agency for Child Development",
	"committee-on-youth-services" : 		"Youth Board, Department of Youth and Community Development, Interagency Coordinating Council on Youth, and youth related programs",
}
