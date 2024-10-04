from flask import Flask, request, jsonify
from patient_service import PatientService

app = Flask(__name__)

patient_service = PatientService()

@app.route('/patients', methods=['GET'])
def get_patients():
    patients = patient_service.get_all_patients()
    return jsonify([patient.to_dict() for patient in patients])

@app.route('/patients/<int:patient_id>', methods=['GET'])
def get_patient(patient_id: int):
    patient = patient_service.get_patient(patient_id)
    if patient:
        return jsonify(patient.to_dict())
    else:
        return jsonify({'error': 'Patient not found'}), 404

@app.route('/patients', methods=['POST'])
def create_patient():
    patient_data = request.get_json()
    patient = Patient(**patient_data)
    patient_service.add_patient(patient)
    return jsonify(patient.to_dict()), 201

@app.route('/patients/<int:patient_id>', methods=['PUT'])
def update_patient(patient_id: int):
    patient_data = request.get_json()
    patient = patient_service.get_patient(patient_id)
    if patient:
        patient_service.update_patient(patient_id, Patient(**patient_data))
        return jsonify(patient.to_dict())
    else:
        return jsonify({'error': 'Patient not found'}), 404

@app.route('/patients/<int:patient_id>', methods=['DELETE'])
def delete_patient(patient_id: int):
    patient_service.delete_patient(patient_id)
    return jsonify({'message': 'Patient deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)
