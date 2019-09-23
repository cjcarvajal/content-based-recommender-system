#!flask/bin/python
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from flask import request
from persistence_manager import PersistenceManager
from cosine_similitude_calculator import CosineSimilitudeCalculator

app = Flask(__name__)
CORS(app,resources=r'/*')

pm = PersistenceManager()
cosine_calculator = CosineSimilitudeCalculator(pm.keywords_dict)

@app.route('/item/review',methods=['POST'])
def get_recommendation_by_review():

	item_key = 'item'

	if not request.json or item_key not in request.json:
		return 'Empty payload',400

	item_number = request.json[item_key]
	response = {}
	response['movies'] = []
	response['movies'].append('Ni mierda')
	response['movies'].append('Ni mierda 2')
	response['movies'].append('Ni mierda 3: El juego final')

	print(cosine_calculator.get_similar_items(item_number,20))

	return jsonify(response),200

@app.route('/item',methods=['GET'])
def get_movie_name():
	
	item_id = request.args.get('item_id')
	if not item_id:
		return 'No id was sent',400

	item_name = pm.get_item_name(item_id)

	if not item_name:
		return '',204

	return item_name,200

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8082)
