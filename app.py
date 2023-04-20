from flask import Flask, jsonify, render_template
from db import load_jobs_from_db

app = Flask(__name__)


@app.route("/")
def index():
    page_title = 'Job Listing Portal'
    jobs = load_jobs_from_db()
    return render_template('home.html',
                           title=page_title,
                           jobs=jobs)


@app.route('/api/jobs/')
def job_page():
    jobs = load_jobs_from_db()
    return jsonify(jobs)
