from flask import Blueprint, jsonify, request 
from __init__ import collection
from main_routes import main

main = Blueprint('main', __name__)

@main.route('/')
def index():
    data = 'Hello Backend'
    return jsonify(data), 201

about_me_data = {
    'name': '',
    'course': '',
    'year': '',
    'ccas': ''
}

@main.route('/about_me', methods=['GET', 'POST'])
def about_us():
    if request.method == 'GET':
        return jsonify(about_me_data), 200

    if request.method == 'POST':
        json_data = request.get_json()

        if json_data:
            about_me_data['name'] = json_data.get('Name', '')
            about_me_data['course'] = json_data.get('Course', '')
            about_me_data['year'] = json_data.get('Year', '')
            about_me_data['ccas'] = json_data.get('CCAs', [])

            return jsonify({'message': 'Data received successfully'}), 201
        else:
            return jsonify({'message': 'Invalid JSON data'}), 404

@main.route('/add_item', methods=['POST'])
def add_item():
    try:
        if request.method == "POST":
            print("Received POST Request")
            return "Done", 201 
    except Exception as e:
        print(f"Error : {e}") 
    return "Can't add", 404