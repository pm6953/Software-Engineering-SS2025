#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, request, jsonify
from flask import render_template

app = Flask(__name__)

# GET all persons
@app.route('/person/', methods=['GET'])
def get_persons():
    with open('data.json', 'r') as f:
        data = f.read()
        return data


# POST (create a new person)
@app.route('/person/<first_name>/<last_name>', methods=['PUT'])
def create_person():
    record = json.loads(request.data)
    with open('data.json', 'r') as f:
        data = f.read()
    if not data:
        records = [record]
    else:
        records = json.loads(data)
        records.append(record)
    with open('data.json', 'w') as f:
        f.write(json.dumps(records, indent=2))
    response = jsonify(record)
    response.status_code = 201
    response.headers['Location'] = f"/person/{record['id']}"
    return response

# GET a person by id
@app.route('/person/<id>', methods=['GET'])
def get_person(id):

    with open('data.json', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for record in records:
            if record['id'] == id:
                return jsonify(record)
        return jsonify({'error': 'data not found'})
    
# PUT (update a person)
@app.route('/person/<id>', methods=['PUT'])

def update_person(id):
    record = json.loads(request.data)
    with open('data.json', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for i in range(len(records)):
            if records[i]['id'] == id:
                records[i] = record
                with open('data.json', 'w') as f:
                    f.write(json.dumps(records, indent=2))
                return jsonify(record)
        return jsonify({'error': 'data not found'})

# DELETE a person
@app.route('/person/<id>', methods=['DELETE'])

def delete_person(id):

    with open('data.json', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for i in range(len(records)):
            if records[i]['id'] == id:
                record = records.pop(i)
                with open('data.json', 'w') as f:
                    f.write(json.dumps(records, indent=2))
                record["deleted"] = "True"
                return jsonify(record)
        return jsonify({'error': 'data not found'})


# GET all persons
@app.route('/', methods=['GET'])
def landing_page():
    return render_template('index.html')

app.run(debug=True)