from flask import Flask, jsonify, send_file, request, send_from_directory, current_app
import random
from flask import request
from flask.ext.restful import Api, Resource
from flask.ext.sqlalchemy import SQLAlchemy
from db.models import db_connect
from sqlalchemy import text
from yelp_client import YelpClient
import json

app = Flask(__name__)
app.debug = True
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://uzqlfkmjghlxqf:PtM-eop0Gse4fH5W7taOPKrbtX@ec2-54-235-207-226.compute-1.amazonaws.com:5432/db7t89tu8f2tu4'
engine = db_connect()

@app.route('/businesses')
def api_businesses():
    query = text('SELECT b.business_id as id, b.name, b.longitude, b.latitude, b.categories, b.attributes, v.minor_violation_score, v.major_violation_score,v.serve_violation_score from businesses as b inner join maps as m on m.business_id = b.business_id inner join violations as v on v.restaurant_id = m.restaurant_id')
    violations = engine.execute(query)
    result =  json.dumps({'businesses':[dict(r) for r in violations]})
    return result

@app.route('/test')
def api_test():
    query = text('SELECT * from businesses')
    res = engine.execute(query)
    return json.dumps([dict(r) for r in res])

@app.route('/search',methods=['GET'])
def api_search():
    """Search for a restaurant with its business id (end of yelp url)
    YelpClient can find at yelp_client.py
    """

    name = request.args.get('name')
    client = YelpClient()
    response = client.search(name).business
    res = {
            "name" : response.name,
            "rating" :response.rating,
            "lat" : response.location.coordinate.latitude,
            "lng" : response.location.coordinate.longitude,
            "categories" : response.categories,
            "violation_major_score" : random.randrange(10),
            "violation_minor_score" : random.randrange(15),
            "violation_serve_score" : random.randrange(6)
            }
    return json.dumps(res)


@app.route('/')
def index():
    return send_from_directory(current_app._static_folder,'index.html')

if __name__ == '__main__':
    app.run()

