import csv
from flask import Flask 
from helpers import get_data
from flask import render_template
app = Flask(__name__)

@app.route("/")
def homepage():
	template = 'homepage.html'
	object_list = get_data()
	return render_template(template)

@app.route('/<row_id>/')
def detail(row_id):
    template = 'results.html'
    object_list = get_data()
    for row in object_list:
        if row['record_key'] == row_id:
           return render_template(template, object=row)
    abort(404)

if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)

