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
	tail_length_key = 'recommendations'

	if not request.json or item_key not in request.json:
		return 'Empty payload',400

	item_number = request.json[item_key]

	if tail_length_key in request.json:
		recommendations_length = request.json[tail_length_key]
	else:
		recommendations_length = 20

	item = pm.get_item(item_number)

	if item.empty:
		return 'Invalid item',400

	item_indexes = cosine_calculator.get_similar_items(item.index.item(),recommendations_length)

	response = {}
	response['movies'] = []

	for i in item_indexes:
		response['movies'].append(pm.get_item_by_internal_id(i))

	return jsonify(response),200

@app.route('/item',methods=['GET'])
def get_movie_name():
	
	item_id = request.args.get('item_id')
	if not item_id:
		return 'No id was sent',400

	item = pm.get_item(item_id)

	if item.empty:
		return '',204

	return item.original_title.iloc[0],200

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8082)
