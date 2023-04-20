from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()
db_host = os.environ.get('DB_HOST')
db_username = os.environ.get('DB_USERNAME')
db_password = os.environ.get('DB_PASSWORD')
db_database = os.environ.get('DB_DATABASE')

db_details = f"mysql+pymysql://{db_username}:{db_password}@{db_host}/{db_database}?charset=utf8mb4"

engine = create_engine(
    db_details,
    connect_args={
        "ssl": {
            "ca": "/etc/ssl/certs/ca-certificates.crt"
        }
    }
)


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM jobs")
        )
        jobs = result.fetchall()
        return jobs


def load_job_from_db(id):
    with engine.connect() as conn:
        job = conn.execute(
            text(f"SELECT * FROM jobs WHERE id = {id}")
        ).fetchone()
        return job
