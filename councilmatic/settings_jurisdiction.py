# These are all the settings that are specific to a jurisdiction

###############################
# These settings are required #
###############################

CITY_NAME = 'New York City'
CITY_NAME_SHORT = 'NYC'
CITY_COUNCIL_NAME = 'New York City Council'
OCD_JURISDICTION_ID = 'ocd-jurisdiction/country:us/state:ny/place:new_york/government'
OCD_CITY_COUNCIL_ID = 'ocd-organization/0f63aae8-16fd-4d3c-b525-00747a482cf9'

LEGISLATIVE_SESSIONS = ['2014'] # the last one in this list should be the current legislative session

APP_NAME = 'nyc'

# VOCAB SETTINGS FOR FRONT-END DISPLAY
CITY_VOCAB = {
    'MUNICIPAL_DISTRICT': 'District',       # e.g. 'District'
    'SOURCE': 'City Council',
    'COUNCIL_MEMBER': 'Council Member',       # e.g. 'Council Member'
    'COUNCIL_MEMBERS': 'Council Members',      # e.g. 'Council Members'
    'EVENTS': 'Meetings',               # label for the events listing, e.g. 'Events'
}


#########################
# The rest are optional #
#########################

# this is for populating meta tags
SITE_META = {
    'site_name' : 'NYC Councilmatic',
    'site_desc' : 'New York City Council, demystified. Keep tabs on what your local representatives are up to.',
    'site_author' : 'PPF & DataMade',
    'site_url' : 'http://nyc.councilmatic.org',
    'twitter_site': '@ppolitics',
    'twitter_creator': '@DataMadeCo',
}


LEGISTAR_URL = 'http://legistar.council.nyc.gov/Legislation.aspx'



# this is for the boundaries of municipal districts, to add
# shapes to posts & ultimately display a map with the council
# member listing. the boundary set should be the relevant
# slug from the ocd api's boundary service
# available boundary sets here: http://ocd.datamade.us/boundary-sets/
BOUNDARY_SET = 'nyc-council-districts'

# this is for configuring a map of council districts using data from the posts
# set MAP_CONFIG = None to hide map
MAP_CONFIG = {
    'center': [40.7127, -74.0059],
    'zoom': 10,
    'color': "#3D8A8E", #teal
    'highlight_color': "#EB6864", #salmon
}




FOOTER_CREDITS = [
    {
        'name':     'The Participatory Politics Foundation',
        'url':      'http://www.participatorypolitics.org/',
        'image':    'ppf-logo.png',
    },
    {
        'name':     'The Rita Allen Foundation',
        'url':      'http://www.ritaallen.org/',
        'image':    'rita-allen-logo.png',
    },
    {
        'name':     'DataMade',
        'url':      'http://datamade.us/',
        'image':    'datamade-logo.png',
    },
]

# this is the default text in search bars
SEARCH_PLACEHOLDER_TEXT = "Taxi, Resolution 815-2015, etc."



# these should live in APP_NAME/static/
IMAGES = {
    'logo': 'images/logo.png',
}
# you can generate icons from the logo at http://www.favicomatic.com/
# & put them in APP_NAME/static/images/icons/


# this is the name of the meetings where the entire city council meets
# as stored in legistar
CITY_COUNCIL_MEETING_NAME = 'City Council Stated Meeting'

# this is the name of the role of committee chairs, e.g. 'CHAIRPERSON' or 'Chair'
# as stored in legistar
# if this is set, committees will display chairs
COMMITTEE_CHAIR_TITLE = 'CHAIRPERSON'

# this is the anme of the role of committee members,
# as stored in legistar
COMMITTEE_MEMBER_TITLE = 'Committee Member'



# this is for convenience, & used to populate a table
# describing legislation types on the about page template
LEGISLATION_TYPE_DESCRIPTIONS = [
    {
        'name': 'Introduction',
        'search_term': 'introduction',
        'fa_icon': 'file-text-o',
        'html_desc': True,
        'desc': 'A proposal for a NYC local law. <br/>\
                Ways for an introduction to become a local law: <ul><li>the Council approves & the Mayor approves,</li> \
                <li>the Mayor vetoes & the Council achieves 2/3 vote within 30 days, or</li>\
                <li>the Council approves & the Mayor does not act within 30 days</li></ul>',

    },
    {
        'name': 'Resolution',
        'search_term': 'resolution',
        'fa_icon': 'commenting-o',
        'html_desc': True,
        'desc': "An expression of the Council's opinion on public policy issues that may or may not fall under City jurisdiction. \
                Resolutions can be used to: <ul><li>support/oppose federal or state legislation,</li>\
                <li>commemorate people and events, or</li>\
                <li>adopt budget and land use items</li></ul>",
    },
    {
        'name': 'SLR (State Legislation Resolution)',
        'search_term': 'slr',
        'fa_icon': 'commenting-o',
        'html_desc': False,
        'desc': 'A special resolution that serves as an official home rule request from the Council to the State Senate and State Assembly to pass pending legislation in the New York State Legislature. The initial request for a SLR must come from the Legislature in Albany.',
    },
    {
        'name': 'Land Use Application',
        'search_term': 'land use application',
        'fa_icon': 'building-o',
        'html_desc': False,
        'desc': 'Land use proposals to be considered by the Council’s Land Use Committee',
    },
    {
        'name': 'Land Use Call-Up',
        'search_term': 'land use call-up',
        'fa_icon': 'building-o',
        'html_desc': False,
        'desc': "Land use proposals that don't require Council approval, but have been chosen by a Council Member for discretionary Council review.",
    },
    {
        'name': 'Mayor’s Messages',
        'search_term': "mayor's message",
        'fa_icon': 'bullhorn',
        'html_desc': False,
        'desc': 'Communications from the Mayor. These generally include appointments to boards and commissions, as well as veto messages.',
    },
    {
        'name': 'Communications',
        'search_term': 'communication',
        'fa_icon': 'bullhorn',
        'html_desc': False,
        'desc': 'Communications from the City, County or Borough offices. These usually concern appointments to boards and commissions.',
    },
    {
        'name': 'Petitions',
        'search_term': 'petition',
        'fa_icon': 'bullhorn',
        'html_desc': False,
        'desc': 'Communication from individuals or entities other than the Mayor, City, County or Borough Offices. These generally include communications from the City Council, and usually concern City Council appointments and resignations.',
    },
]
ABOUT_BLURBS = {
    "COMMITTEES" : "<p>Most of the Council's legislative work is done in committee. It is there that proposed legislation is initially debated and the members of other government branches and the public are given a chance to comment.</p>\
                    <p>Each Council Member serves on at least three of the Council's standing committees, sub- and select committees and panels. The standing committees must meet at least once a month unless the Charter mandates otherwise. Committee assignments are made by the Committee on Rules, Privileges and Elections and voted on by the entire Council.</p>\
                    <p>New York City Council is currently composed of 38 Committees and 6 Subcommittees.</p>",
    "EVENTS":       "<p>Most of the Council's legislative action happens in committees. Each committee meets in public hearings 2-3 times per month where proposed legislation is debated. Members of other government branches, as well as the public, are able to attend and comment at these hearings.</p>\
                    <p>Meetings of the entire Council, referred to as Stated Meetings, occur twice a month at City Hall. </p>",
    "COUNCIL_MEMBERS": ""

}

# these keys should match committee slugs
COMMITTEE_DESCRIPTIONS = {
    "committee-on-aging" :                  "Department for the Aging and all federal, state and municipal programs pertinent to senior citizens",
    "committee-on-civil-rights" :           "Human Rights Commission, Equal Employment Practices Commission and Equal Employment Opportunity",
    "committee-on-civil-service-and-labor" : "Municipal Officers and Employees, Office of Labor Relations, Office of Collective Bargaining, Office of Labor Services, and Municipal Pension and Retirement Systems",
    "committee-on-community-development" :  "Issues relating to poverty and its reduction especially in low income neighborhoods",
    "committee-on-consumer-affairs" :       "Department of Consumer Affairs",
    "committee-on-contracts" :              "Procurement Policy Board, review of City procurement policies and procedures, oversight over government contracts, Mayor's Office of Contract Services and collection agency contracts",
    "committee-on-courts-and-legal-services" : "Courts and Legal Aid",
    "committee-on-cultural-affairs-libraries-and-international-intergroup-relations" : "Department of Cultural Affairs, libraries, museums, Art Commission, New York City Commission for the United Nations, Consular Corps and Protocol, Mayor’s Office of Special Projects and Community Events, and to encourage harmony among the citizens of New York City, to promote the image of New York City and enhance the relationship of its citizens with the international community",
    "committee-on-economic-development" :   "Economic Development Corporation and Department of Small Business Services",
    "committee-on-education" :              "Department of Education, School Construction Authority and charter schools",
    "committee-on-environmental-protection" : "Department of Environmental Protection and Office of Long Term Planning and Sustainability",
    "committee-on-finance" :                "Executive Budget review and Budget modification, Banking Commission, Comptroller's Office, Department of Design and Construction, Department of Finance, Independent Budget Office and fiscal policy and revenue from any source",
    "committee-on-fire-and-criminal-justice-services" : "Fire/EMS (non-health related issues), Department of Probation, Department of Correction, and Emergency Management Department (OEM)",
    "committee-on-general-welfare" :        "Human Resources Administration/Department of Social Services, Administration for Children's Services, Department of Homeless Services, Office of Immigrant Affairs and charitable institutions",
    "committee-on-governmental-operations" : "Municipal governmental structure and organization, Department of Citywide Administrative Services, Community Boards, Tax Commission, Board of Standards and Appeals, Campaign Finance Board, Board of Elections, Voter Assistance Commission, Commission on Public Information and Communication, Department of Records and Information Services, Financial Information Services Agency and Law Department",
    "committee-on-health" :                 "Department of Health and Mental Hygiene, Health and Hospitals Corporation and Office of the Chief Medical Examiner and EMS (health related issues)",
    "committee-on-higher-education" :       "City University of New York",
    "committee-on-housing-and-buildings" :  "Department of Housing Preservation and Development, Department of Buildings and rent regulation",
    "committee-on-immigration" :            "Mayor’s Office of Immigrant Affairs and other matters affecting immigration",
    "committee-on-juvenile-justice" :       "Division of Youth and Family Justice within the Administration for Children’s Services",
    "committee-on-land-use" :               "City Planning Commission, Department of City Planning, Department of Information Technology and Telecommunications, Landmarks Preservation Commission, land use and landmarks review",
    "committee-on-mental-health-developmental-disability-alcoholism-drug-abuse-and-disability-services" : "Department of Health and Mental Hygiene (issues of mental health, developmental disability and alcoholism services) and Mayor’s Office for People with Disabilities",
    "committee-on-mental-health-developmental-disability-alcoholism-substance-abuse-and-disability-services" : "Department of Health and Mental Hygiene (issues of mental health, developmental disability and alcoholism services) and Mayor’s Office for People with Disabilities",
    "committee-on-oversight-and-investigations" : "To investigate any matters within the jurisdiction of the Council relating to property, affairs, or government of New York City and the Department of Investigation",
    "committee-on-parks-and-recreation" :   "Department of Parks and Recreation",
    "committee-on-public-housing" :         "NYC Housing Authority",
    "committee-on-public-safety" :          "Police Department, District Attorneys, Special Narcotics Prosecutor, Civilian Complaint Review Board, and Criminal Justice Coordinator",
    "committee-on-recovery-and-resiliency" : "Office of Recovery and Resiliency, issues relating to recovery in Hurricane Sandy affected communities, including the Build It Back Program, and the Office of Long Term Planning and Sustainability as it relates to efforts to make New York City more resilient in the face of climate change, and preparing for, responding to, and recovering from emergencies",
    "committee-on-rules-privileges-and-elections" : "Council structure and organization and appointments",
    "committee-on-sanitation-and-solid-waste-management" : "Department of Sanitation and the Business Integrity Commission",
    "committee-on-small-business" :         "Matters relating to retail business and emerging industries",
    "committee-on-standards-and-ethics" :   "Conflicts of Interest Board and Council Ethics",
    "committee-on-state-and-federal-legislation" : "Federal legislation, State legislation and Home Rule requests",
    "committee-on-technology":              "Technology in New York City, Department of Information Technology and Telecommunications (non-land use-related issues), Mayor’s Office of Media & Entertainment, NYC TV and dissemination of public information through the use of technology",
    "committee-on-transportation" :         "Mass Transportation Agencies and facilities, Department of Transportation, New York City Transit Authority and Taxi and Limousine Commission",
    "committee-on-veterans" :               "Mayor’s Office of Veterans Affairs and other veteran related issues",
    "committee-on-waterfronts" :            "Matters relating to the waterfront",
    "committee-on-womens-issues" :      "Issues relating to public policy concerns of women, domestic violence, Office to Combat Domestic Violence and Agency for Child Development",
    "committee-on-youth-services" :         "Youth Board, Department of Youth and Community Development, Interagency Coordinating Council on Youth, and youth related programs",
}



ABOUT_BLURBS = {
    "COMMITTEES":       "",
    "EVENTS":           "",
    "COUNCIL_MEMBERS":  "",
}
