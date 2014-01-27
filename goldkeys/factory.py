from goldkeys import app

from cors import crossdomain
from authentication import requires_auth
from flask import request
from data import all_factories
import json

@app.route('/factory')
@crossdomain(origin="*")
# @requires_auth
def fetch_all_factories():
	return json.dumps(all_factories())
