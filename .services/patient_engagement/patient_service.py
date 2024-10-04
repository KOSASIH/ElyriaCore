from typing import List
from patient_entity import Patient

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

    def send_reminders(self):
        # Implement reminder sending logic here
        pass

    def send_notifications(self):
        # Implement notification sending logic here
        pass

    def track_engagement(self):
        # Implement engagement tracking logic here
        pass
