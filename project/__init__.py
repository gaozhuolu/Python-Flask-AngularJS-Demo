__author__ = 'David Lu'

#import json
import logging
import urllib
import os
import uuid
import math

from flask import Flask, request, jsonify, session
# from werkzeug import secure_filename
# from bson.objectid import ObjectId
# from flask_bcrypt import Bcrypt
# from pymongo import MongoClient

from project.config import BaseConfig

# from flask.json import JSONEncoder
# class CustomJSONEncoder(JSONEncoder):
#     def default(self, o):
#         if isinstance(o, ObjectId):
#             return str(o)
#         return JSONEncoder.default(self, o)

# config
app = Flask(__name__)
# app.json_encoder = CustomJSONEncoder
app.config.from_object(BaseConfig)
logger = logging.getLogger(__name__)
# bcrypt = Bcrypt(app)

# dbuser = app.config['MONGODB_USER']
# dbpasswd = urllib.quote_plus(app.config['MONGODB_PWD'])
# client = MongoClient('mongodb://' + dbuser + ':' + dbpasswd + '@' + app.config['MONGODB_HOSTNAME'])

# db = client.demodb

# models

# scripts
# from scripts import pe_utils


# routes
@app.route('/')
def index():
	return app.send_static_file('index.html')


# import requests
# from bs4 import BeautifulSoup
@app.route('/api/getaddresslist', methods=['POST'])
def getAddressList():
	# DB Convert implement
	# campaignlist = db.Campaign.find()
	# campid = 1
	# for v in list(campaignlist):
	# 	db.Campaign.update_one(
	# 		{'_id': v['_id']},
	# 		{'$set': {'campid': campid}}
	# 	)
	# 	campid += 1

	return jsonify(
		{
			'list': []
		}
	)
	pass

	# json_data = request.json
	# s = requests.Session()
	# s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
	# payload = urllib.urlencode({'items': 9999, 'page': 1, 'address1': json_data['straddress'], 'city': json_data['strcity'], 'state': json_data['strstate'], 'zip': json_data['strzip']})
	# r = s.get('https://tools.usps.com/go/ZipLookupResultsAction!input.action', params=payload)
    #
	# soup = BeautifulSoup(r.content, 'html.parser')
	# address1_range = soup.find_all(class_="address1 range")
	# city_range = soup.find_all(class_="city range")
	# state_range = soup.find_all(class_="state range")
	# zip = soup.find_all(class_="zip")
	# zip4 = soup.find_all(class_="zip4")
    #
	# result = []
	# for i in range(0, len(address1_range)):
	# 	result.append({'address': address1_range[i].get_text(), 'city': city_range[i].get_text(), 'state': state_range[i].get_text(), 'zipcode': zip[i].get_text() + '-' + zip4[i].get_text()})
    #
	# return jsonify(
	# 	{
	# 		'list': result
	# 	}
	# )