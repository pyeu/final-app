import csv
from flask import Flask
from helpers import get_data, sort_by_criteria
from collections import Counter
from flask import render_template, request

app = Flask(__name__)

inmates = get_data()

@app.route("/about/")
def about():
	return render_template('about.html')

@app.route("/")
def homepage():

	manner_of_death = Counter([d['manner_of_death'] for d in inmates])
	manners_list = manner_of_death.most_common()
	top_manners = manners_list[0:5]

	county_of_death = Counter([d['county'] for d in inmates])
	counties_list = county_of_death.most_common()
	top_counties = counties_list[0:5]

	location_of_death = Counter([d['agency_name'] for d in inmates])
	locations_list = location_of_death.most_common()
	top_locations = locations_list[0:5]

	return render_template('homepage.html',
							top_manners=top_manners,
							top_counties=top_counties,
							top_locations=top_locations,
							inmate_count = len(inmates),
							top_inmates=inmates[0:20])

@app.route('/results/')
def results():
	inmate_name = request.args['partial_name']
	#_sortby = reqargs.get['sortby']

	filtered_inmates = []
	for row in inmates:
		if inmate_name.upper() in row['full_name'].upper():
			filtered_inmates.append(row)
	#filtered_data = sort_by_criteria(criteria=inmate_name, inmates=inmates)

	return render_template('results.html', inmates=filtered_inmates)

@app.route('/county/<county>')
def county_page(county):
	filtered_inmates = []
	for row in inmates:
		if county.upper() in row['county'].upper():
			filtered_inmates.append(row)
	return render_template('results.html', inmates=filtered_data)

@app.route('/testchart')
def test_chart():
	manner_of_death = Counter([d['manner_of_death'] for d in inmates])
	manners_list = manner_of_death.most_common()

	county_of_death = Counter([d['county'] for d in inmates])
	counties_list = county_of_death.most_common()
	major_counties = counties_list[0:20]

	location_of_death = Counter([d['agency_name'] for d in inmates])
	locations_list = location_of_death.most_common()
	major_locations = locations_list[0:20]
	
	return render_template('testchart.html', countydeaths=counties_list,
							major_counties=major_counties, 
							institutiondeaths=locations_list,
							mannersdeath=manners_list,
							major_locations=major_locations)


if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)

