from sqlalchemy import create_engine, text

db_details = "mysql+pymysql://efig7vyreytp16ikh2j9:pscale_pw_knW8lLjwcfaaoIl7fSt76huUtxWMwcVSzA7XU0wrknV@aws.connect.psdb.cloud/job-listing?charset=utf8mb4"

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
