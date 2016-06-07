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

BEST_FIELDS = ['full_name', 'age', 'agency_name',
	'birthday', 'race', 'custody_status', 'custody_offense',
	'date_of_death', 'custodial_responsibility_at_time_of_death', 
	'location_where_cause_of_death_occurred', 'custody_name',
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

	data['age'] = ((data['date_of_death'] - data['birthday']).dt.days / 365).round(0)
	data['full_name'] = data['first_name'].astype(str) + ' ' + data['last_name'].astype(str)

	return data

def sort_by_criteria(criteria, inmates):
    if criteria == 'youngest':
    	rows = sorted(inmates, key=itemgetter('age'))
    elif criteria == 'oldest':
        rows = sorted(inmates, key=itemgetter('age'), reverse=True)
    elif criteria == 'most_oldest':
        rows = sorted(inmates, key=itemgetter('date_of_death'))
    else:
    #i.e. 'most_recent' or any value...just sort by most recent
        rows = sorted(inmates, key=itemgetter('date_of_death'), reverse=True)   
    return rows