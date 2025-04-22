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
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/person', methods=['PUT'])
def create_person():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Keine Daten erhalten"}), 400
    # Überprüfe, ob alle erforderlichen Felder vorhanden sind
    required_fields = ["first_name", "last_name", "date_of_birth", "sex", "email"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Feld {field} fehlt"}), 400
    return jsonify({"message": "Person erfolgreich angelegt", "data": data}), 201

if __name__ == "__main__":
    app.run(debug=True)

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