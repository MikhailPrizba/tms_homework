import datetime

import requests
from flask import Blueprint

app1 = Blueprint('site', __name__)

@app1.route('/time')
def current_time():
    return datetime.datetime.now().time().isoformat()

@app1.route('/quote')
def quote():
    return requests.get('https://api.kanye.rest/').text



