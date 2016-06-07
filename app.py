import csv
from flask import Flask 
from helpers import get_data
from collections import Counter
from flask import render_template, request
app = Flask(__name__)

inmates = get_data()

@app.route("/")
def homepage():
	

	manner_of_death = Counter([d['manner_of_death'] for d in inmates])
	manners_list = manner_of_death.most_common()



	return render_template('homepage.html', 
							manners_list=manners_list,
							inmate_count = len(inmates), 
							top_inmates=inmates[0:20])

@app.route('/results/')
def results():
	inmate_name = request.args['partial_name']

	filtered_inmates = []
	for row in inmates:
		if inmate_name.upper() in row['full_name'].upper():
			filtered_inmates.append(row)
	return render_template('results.html', inmates=filtered_inmates)

if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)

