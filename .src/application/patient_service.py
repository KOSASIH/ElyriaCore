from typing import List
from domain.patient import Patient
from domain.medical_record import MedicalRecord

class PatientService:
    def __init__(self):
        self.patients = []

    def add_patient(self, patient: Patient):
        self.patients.append(patient)

    def get_patient(self, patient_id: int) -> Patient:
        for patient in self.patients:
            if patient.id == patient_id:
                return patient
        return None

    def update_patient(self, patient_id: int, patient: Patient):
        for i, existing_patient in enumerate(self.patients):
            if existing_patient.id == patient_id:
                self.patients[i] = patient
                break

    def delete_patient(self, patient_id: int):
        for i, patient in enumerate(self.patients):
            if patient.id == patient_id:
                del self.patients[i]
                break

    def get_all_patients(self) -> List[Patient]:
        return self.patients

    def create_medical_record(self, patient_id: int, medical_record: MedicalRecord):
        patient = self.get_patient(patient_id)
        if patient:
            patient.medical_records.append(medical_record)
            return medical_record
        else:
            return None

    def get_medical_record(self, patient_id: int, medical_record_id: int) -> MedicalRecord:
        patient = self.get_patient(patient_id)
        if patient:
            for medical_record in patient.medical_records:
                if medical_record.id == medical_record_id:
                    return medical_record
        return None

    def update_medical_record(self, patient_id: int, medical_record_id: int, medical_record: MedicalRecord):
        patient = self.get_patient(patient_id)
        if patient:
            for i, existing_medical_record in enumerate(patient.medical_records):
                if existing_medical_record.id == medical_record_id:
                    patient.medical_records[i] = medical_record
                    break
        return None

    def delete_medical_record(self, patient_id: int, medical_record_id: int):
        patient = self.get_patient(patient_id)
        if patient:
            for i, medical_record in enumerate(patient.medical_records):
                if medical_record.id == medical_record_id:
                    del patient.medical_records[i]
                    break
        return None
