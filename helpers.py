import csv
import requests
import pandas as pd
from os.path import join
from operator import itemgetter
from datetime import datetime

custody_data_fname = './static/data/Death_in_Custody_2013.csv'
offense_codes_fname = './static/data/Data_Codes.csv'
location_codes_fname = './static/data/location_codes.csv'
counties_fname = './static/data/counties.txt'
#DATA_FPATH_4 = geosomething 

# BEST_FIELDS = ['reporting_agency', 'last_name', 'first_name', 
# 	'middle_name', 'date_of_birth_mm', 'date_of_birth_dd', 
# 	'date_of_birth_yyyy', 'race', 'custody_status', 'custody_offense',
# 	'date_of_death_yyyy', 'date_of_death_mm', 'date_of_death_dd', 
# 	'custodial_responsibility_at_time_of_death', 
# 	'location_where_cause_of_death_occurred', 'facility_death_occured',
# 	'manner_of_death', 'means_of_death', 'county', 'agency_number']

BEST_FIELDS = ['full_name', 
	'birthday', 'race', 'custody_status', 'custody_offense',
	'date_of_death', 'custodial_responsibility_at_time_of_death', 
	'location_where_cause_of_death_occurred', 'agency_name',
	'manner_of_death', 'means_of_death', 'county']

def get_counties():
	df = pd.read_csv(counties_fname, sep='\t')
	return df.to_dict('records')

def get_data():
    data = join()
    data = add_variables(data)
    data = trim(data)
    normal_data = data.to_dict('records')
    return normal_data

def join():
	deaths = pd.read_csv(custody_data_fname)
	codes = pd.read_csv(offense_codes_fname)
	locations = pd.read_csv(location_codes_fname, encoding="latin-1")
	#names = pd.read_csv(DATA_FPATH_4)
	temp = pd.merge(deaths, codes, on='custody_offense')
	dfa = pd.merge(temp, locations, on='agency_number')
	
	return dfa

def trim(data):
	return data[BEST_FIELDS]

def add_variables(data):
	data['birthday'] = data['date_of_birth_yyyy'].astype(str) + '-' + data['date_of_birth_mm'].astype(str) + '-' + data['date_of_birth_dd'].astype(str)
	data['birthday'] = pd.to_datetime(data['birthday'])
	
	data['date_of_death'] = data['date_of_death_yyyy'].astype(str) + '-' + data['date_of_death_mm'].astype(str) + '-' + data['date_of_death_dd'].astype(str)
	data['date_of_death'] = pd.to_datetime(data['date_of_death'])

	data['age'] = ((data['date_of_death'] - data['birthday']).dt.days / 365).round()
	data['full_name'] = data['first_name'].astype(str) + ' ' + data['last_name'].astype(str)

	return data

def sort_by_criteria(criteria, datarows):
    if criteria == 'youngest':
        rows = sorted(datarows, key=itemgetter('age'))
    elif criteria == 'oldest':
        rows = sorted(datarows, key=itemgetter('age'), reverse=True)
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
