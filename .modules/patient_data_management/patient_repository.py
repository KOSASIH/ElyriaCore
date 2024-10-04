from typing import List
from patient_entity import Patient

class PatientRepository:
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

    def save_to_database(self):
        # Implement database saving logic here
        pass

    def load_from_database(self):
        # Implement database loading logic here
        pass
