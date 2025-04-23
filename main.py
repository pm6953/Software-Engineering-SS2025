#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Hilfsfunktion: Lade Daten aus der Datei
def load_data():
    try:
        with open('data.json', 'r') as f:
            data = f.read()
            return json.loads(data) if data else []
    except FileNotFoundError:
        return []

# Hilfsfunktion: Speichere Daten in die Datei
def save_data(records):
    with open('data.json', 'w') as f:
        f.write(json.dumps(records, indent=2))

# GET all persons
@app.route('/person', methods=['GET'])
def get_persons():
    records = load_data()
    return jsonify(records), 200

# GET a person by ID
@app.route('/person/<id>', methods=['GET'])
def get_person(id):
    records = load_data()
    for record in records:
        if record['id'] == id:
            return jsonify(record), 200
    return jsonify({'error': 'data not found'}), 404

# POST (create a new person)
@app.route('/person', methods=['POST'])
def create_person():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Keine Daten erhalten"}), 400

    # Überprüfe, ob alle erforderlichen Felder vorhanden sind
    required_fields = ["id", "first_name", "last_name", "date_of_birth", "sex", "email"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Feld {field} fehlt"}), 400

    records = load_data()
    # Überprüfe, ob die ID bereits existiert
    for record in records:
        if record['id'] == data['id']:
            return jsonify({"error": "ID existiert bereits"}), 400

    records.append(data)
    save_data(records)
    return jsonify({"message": "Person erfolgreich angelegt", "data": data}), 201

# PUT (update a person)
@app.route('/person/<id>', methods=['PUT'])
def update_person(id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "Keine Daten erhalten"}), 400

    records = load_data()
    for i in range(len(records)):
        if records[i]['id'] == id:
            records[i].update(data)
            save_data(records)
            return jsonify({"message": "Person erfolgreich aktualisiert", "data": records[i]}), 200

    return jsonify({'error': 'data not found'}), 404

# DELETE a person
@app.route('/person/<id>', methods=['DELETE'])
def delete_person(id):
    records = load_data()
    for i in range(len(records)):
        if records[i]['id'] == id:
            record = records.pop(i)
            save_data(records)
            record["deleted"] = "True"
            return jsonify({"message": "Person erfolgreich gelöscht", "data": record}), 200

    return jsonify({'error': 'data not found'}), 404

# Landing Page
@app.route('/', methods=['GET'])
def landing_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)