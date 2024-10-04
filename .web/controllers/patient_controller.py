from flask import Flask, request, jsonify
from domain.patient import Patient
from interface.patient_repository import PatientRepository
from utils.error_handling import handle_error

app = Flask(__name__)

patient_repository = PatientRepository()

@app.route('/patients', methods=['POST'])
def create_patient():
    try:
        patient_data = request.get_json()
        patient = Patient(**patient_data)
        patient_repository.add_patient(patient)
        return jsonify(patient.to_dict()), 201
    except Exception as e:
        handle_error(e)
        return jsonify({'error': 'Failed to create patient'}), 500

@app.route('/patients', methods=['GET'])
def get_patients():
    try:
        patients = patient_repository.get_all_patients()
        return jsonify([patient.to_dict() for patient in patients])
    except Exception as e:
        handle_error(e)
        return jsonify({'error': 'Failed to get patients'}), 500

@app.route('/patients/<int:patient_id>', methods=['GET'])
def get_patient(patient_id):
    try:
        patient = patient_repository.get_patient(patient_id)
        if patient:
            return jsonify(patient.to_dict())
        else:
            return jsonify({'error': 'Patient not found'}), 404
    except Exception as e:
        handle_error(e)
        return jsonify({'error': 'Failed to get patient'}), 500

@app.route('/patients/<int:patient_id>', methods=['PUT'])
def update_patient(patient_id):
    try:
        patient_data = request.get_json()
        patient = patient_repository.get_patient(patient_id)
        if patient:
            patient_repository.update_patient(patient_id, Patient(**patient_data))
            return jsonify(patient.to_dict())
        else:
            return jsonify({'error': 'Patient not found'}), 404
    except Exception as e:
        handle_error(e)
        return jsonify({'error': 'Failed to update patient'}), 500

@app.route('/patients/<int:patient_id>', methods=['DELETE'])
def delete_patient(patient_id):
    try:
        patient_repository.delete_patient(patient_id)
        return jsonify({'message': 'Patient deleted'})
    except Exception as e:
        handle_error(e)
        return jsonify({'error': 'Failed to delete patient'}), 500
