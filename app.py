from flask import Flask, jsonify, render_template

app = Flask(__name__)

jobs = [
    {
        "id": 1,
        "title": "Software Engineer",
        "location": "San Francisco, CA",
        "salary": 120000
    },
    {
        "id": 2,
        "title": "Product Manager",
        "location": "New York, NY",
        "salary": 130000
    },
    {
        "id": 3,
        "title": "Data Scientist",
        "location": "Seattle, WA",
        "salary": 110000
    },
    {
        "id": 4,
        "title": "Marketing Manager",
        "location": "Chicago, IL",
        "salary": 90000
    },
    {
        "id": 5,
        "title": "UX Designer",
        "location": "Los Angeles, CA",
        "salary": 100000
    },
    {
        "id": 6,
        "title": "Sales Representative",
        "location": "Boston, MA",
        "salary": 80000
    }
]

# Index page
@app.route("/")
def index():
    page_title = 'Job Listing Portal'
    return render_template('home.html',
                           title=page_title,
                           jobs=jobs)

# API for jobs
@app.route('/api/jobs/')
def job_page():
    return jsonify(jobs)
