from app.models import bq_client
from app import app
from flask import render_template

@app.route('/task1')
def show_task_1():
    query = 'SELECT * FROM `bigquery-cc-a1-task2-s3663431.a1_2.top_timeslots_by_tradevalue`'
    rows = bq_client.run_query(query)
    schema = [field.name for field in rows.schema]
    return render_template('index.html', rows=rows, schema=schema)