from flask import Flask, jsonify, render_template, redirect, url_for
from db import load_job_from_db, load_jobs_from_db

app = Flask(__name__)


@app.route("/")
def home():
    jobs = load_jobs_from_db()
    return render_template(
        'home.html',
        title='Home',
        jobs=jobs
    )


@app.route('/api/jobs/')
def job_api():
    jobs = load_jobs_from_db()
    return jsonify(jobs)


@app.route("/job/<int:id>")
def job_details(id):
    job = load_job_from_db(id)

    if not job:
        return redirect(url_for('home'))
    return render_template(
        'job.html',
        job=job
    )
