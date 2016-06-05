import csv
import requests
from os.path import join
from operator import itemgetter

DATA_FNAME_1 = 'Deaths_in_Custody_2013.xlsx'
DATA_FNAME_2 = 'Data_Codes.xlsx'

def get_data(csv_filename):
    # open data file
    # return list of dicts
    csv_path = '/static/{csv_filename}'
    with open(csv_path, 'r') as f:
        c = csv.DictReader(f)
        return list(c)

# def sort_by_criteria(criteria, datarows):
#     if criteria == 'species':
#         rows = sorted(datarows, key=itemgetter('species'))
#     elif criteria == 'custody':
#         rows = sorted(datarows, key=itemgetter('incident_date'))
#     else:
#        # i.e. 'youngest' or any value...just sort by most recent
#         rows = sorted(datarows, key=itemgetter('incident_date'), reverse=True)   
#     return rows

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
