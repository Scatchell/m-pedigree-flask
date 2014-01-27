from goldkeys import app

from cors import crossdomain
from authentication import requires_auth
from flask import request
from data import all_companies
import json

@app.route('/company')
@crossdomain(origin="*", methods="*", headers='Content-Type')
# @requires_auth
def fetch_all_companies():
	return json.dumps(all_companies())

@app.route('/company/<int:company_id>')
@crossdomain(origin="*", methods="*", headers='Content-Type')
# @requires_auth
def fetch_company(company_id):
	for company in all_companies():
		if company['id'] == company_id:
			return json.dumps(company)

@app.route('/company/<int:company_id>', methods = ['POST'])
@crossdomain(origin="*", methods="*", headers='Content-Type')
# @requires_auth
def update_company(company_id):

	company_name = request.json.get('company_name')
	company_code = request.json.get('company_code')

	print "Updating..."

	return company_name