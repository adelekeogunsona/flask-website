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
        result = conn.execute(text("select * from jobs"))
        column_names = result.keys()
        jobs = []
        for row in result.all():
            jobs.append(dict(zip(column_names, row)))
    return jobs
