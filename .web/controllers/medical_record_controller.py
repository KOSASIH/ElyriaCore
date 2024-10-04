from flask import Flask, request, jsonify
from domain.medical_record import MedicalRecord
from interface.medical_record_repository import MedicalRecordRepository
from utils.error_handling import handle_error

app = Flask(__name__)

medical_record_repository = MedicalRecordRepository()

@app.route('/medical-records', methods=['POST'])
def create_medical_record():
    try:
        medical_record_data = request.get_json()
        medical_record = MedicalRecord(**medical_record_data)
        medical_record_repository.add_medical_record(medical_record)
        return jsonify(medical_record.to_dict()), 201
    except Exception as e:
        handle_error(e)
        return jsonify({'error': 'Failed to create medical record'}), 500

@app.route('/medical-records', methods=['GET'])
def get_medical_records():
    try:
        medical_records = medical_record_repository.get_all_medical_records()
        return jsonify([medical_record.to_dict() for medical_record in medical_records])
    except Exception as e:
        handle_error(e)
        return jsonify({'error': 'Failed to get medical records'}), 500

@app.route('/medical-records/<int:medical_record_id>', methods=['GET'])
def get_medical_record(medical_record_id):
    try:
        medical_record = medical_record_repository.get_medical_record(medical_record_id)
        if medical_record:
            return jsonify(medical_record.to_dict())
        else:
            return jsonify({'error': 'Medical record not found'}), 404
    except Exception as e:
        handle_error(e)
        return jsonify({'error': 'Failed to get medical record'}), 500

@app.route('/medical-records/<int:medical_record_id>', methods=['PUT'])
def update_medical_record(medical_record_id):
    try:
        medical_record_data = request.get_json()
        medical_record = medical_record_repository.get_medical_record(medical_record_id)
        if medical_record:
            medical_record_repository.update_medical_record(medical_record_id, MedicalRecord(**medical_record_data))
            return jsonify(medical_record.to_dict())
        else:
            return jsonify({'error': 'Medical record not found'}), 404
    except Exception as e:
        handle_error(e)
        return jsonify({'error': 'Failed to update medical record'}), 500

@app.route('/medical-records/<int:medical_record_id>', methods=['DELETE'])
def delete_medical_record(medical_record_id):
    try:
        medical_record_repository.delete_medical_record(medical_record_id)
        return jsonify({'message': 'Medical record deleted'})
    except Exception as e:
        handle_error(e)
        return jsonify({'error': 'Failed to delete medical record'}), 500
