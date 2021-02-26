from flask import Flask, jsonify, abort, request, url_for

from datetime import datetime

#from cerberus import Validator

app = Flask(__name__)


activity_log = [
    {
        'id': '0',
        'user_id': 1,
        'timestamp': "2021-01-25 22:33:33",
        'details': "Important stuff here",
    },
    {
        'id': '1',
        'user_id': 2,
        'timestamp': "2021-01-25 22:33:33",
        'details': "Even more important",
    },
    {
        'id': '2',
        'user_id': 3,
        'timestamp': "2021-01-25 22:33:33",
        'details': "The most important",
    },
]



#v = Validator(activity_log_schema)
#item['location'] = url_for('activities_by_id',id=item['id'])
@app.route('/api/activities', methods=["GET"])
def activities():
	return jsonify({'activities' : activity_log})

@app.route('/api/activities/<int:id>', methods=["GET"])
def activities_by_id(id):
	if id < 0 or id>=len(activity_log):
		abort(404)
	return jsonify(activity_log[id])

@app.route('/api/activities', methods=["POST"])
def new_activities():
	if not request.json:
		abort(400)
	new_activity = request.get_json()

	if 'id' in new_activity in new_activity:
		abort(400)

	if 'user_id' not in new_activity or 'timestamp' not in new_activity or 'details' not in new_activity:
		abort(400)

	#new_activity['_id'] = "101"
	#new_activity['location'] = url_for('activities_by_id',id=new_activity['id'])
	return jsonify(new_activity), 201
