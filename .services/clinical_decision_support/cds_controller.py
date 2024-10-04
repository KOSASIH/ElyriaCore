from flask import Flask, request, jsonify
from cds_service import CDSService

app = Flask(__name__)

cds_service = CDSService()

@app.route('/cds/rules', methods=['GET'])
def get_rules():
    rules = cds_service.get_rules()
    return jsonify([rule.to_dict() for rule in rules])

@app.route('/cds/rules', methods=['POST'])
def create_rule():
    rule_data = request.get_json()
    rule = Rule(**rule_data)
    cds_service.add_rule(rule)
    return jsonify(rule.to_dict()), 201

@app.route('/cds/patients/<int:patient_id>/recommendations', methods=['GET'])
def get_recommendations(patient_id: int):
    patient = Patient.query.get(patient_id)
    if patient:
        recommendations = cds_service.get_recommendations(patient)
        return jsonify(recommendations)
    else:
        return jsonify({'error': 'Patient not found'}), 404

@app.route('/cds/patients/<int:patient_id>/recommendations', methods=['POST'])
def save_recommendations(patient_id: int):
    patient = Patient.query.get(patient_id)
    if patient:
        recommendations = request.get_json()
        cds_service.save_recommendations(patient, recommendations)
        return jsonify({'message': 'Recommendations saved'}), 200
    else:
        return jsonify({'error': 'Patient not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
