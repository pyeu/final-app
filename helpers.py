import csv
import requests
import pandas as pd
from os.path import join
from operator import itemgetter

DATA_FPATH_1 = './static/data/Death_in_Custody_2013.csv'
DATA_FPATH_2 = './static/data/Data_Codes.csv'
DATA_FPATH_3 = './static/data/location_codes.csv'
#DATA_FPATH_4 = geosomething 

def get_data():
    datafile = join()
    with open(datafile, 'r') as f:
        c = csv.DictReader(f)
        return list(c)

def join():
	deaths = pd.read_csv(DATA_FPATH_1)
	codes = pd.read_csv(DATA_FPATH_2)
	locations = pd.read_csv(DATA_FPATH_3)
	#names = pd.read_csv(DATA_FPATH_4)

	add_continuous_variables()

	dfa = deaths[['reporting_agency', 'last_name', 'first_name', 
	'middle_name', 'date_of_birth_mm', 'date_of_birth_dd', 
	'date_of_birth_yyyy', 'race', 'custody_status', 'custody_offense',
	'date_of_death_yyyy', 'date_of_death_mm', 'date_of_death_dd', 
	'custodial_responsibility_at_time_of_death', 
	'location_where_cause_of_death_occurred', 'facility_death_occured',
	'manner_of_death', 'means_of_death', 'county']]
	dfb = codes[['name', 'custody_offense']]
	dfc = locations[['agency_number', 'agency_name']]

	temp = pd.merge(dfa, dfb, on='custody_offense')
	dfx = pd.merge(temp, dfc, on='agency_number')
	return dfx


def add_continuous_variables():
	


	deaths['days'] = 


# MAKE TWO MORE VARIABLES, date of death and days in custody


def sort_by_criteria(criteria, datarows):
    if criteria == 'days_low':
        rows = sorted(datarows, key=itemgetter('days'))
    elif criteria == 'days_high':
        rows = sorted(datarows, key=itemgetter('days'), reverse=True)
    else:
       # i.e. 'date_recent' or any value...just sort by most recent
        rows = sorted(datarows, key=itemgetter('date_of_death'), reverse=True)   
    return rows

# def get_wiki_photo(txt):
#     a = search_wiki(txt)
#     b = get_wiki_photo_url(a)
#     return b

# def search_wiki(user_input):
#     user_input = user_input.strip().lower().replace(" ", "_")

#     temp_url = "https://en.wikipedia.org/w/api.php?action=opensearch&format=json&formatversion=2&search={term}&namespace=0&limit=10&suggest=true"
#     url = temp_url.format(term=user_input)

#     site = requests.get(url)
#     return site.json()[1][0]

# def get_wiki_photo_url(search_term):
#     temp_url = "https://en.wikipedia.org/w/api.php?action=query&prop=pageimages&format=json&piprop=original&titles={term}"
#     url = temp_url.format(term=search_term)

#     response = requests.get(url)

#     data = response.json()

#     x = list(data['query']['pages'].values())
#     photo_url = x[0]['thumbnail']['original']

#     return photo_url
