from . import client

def run_query(query):
    q = client.query(query)
    return q.result()