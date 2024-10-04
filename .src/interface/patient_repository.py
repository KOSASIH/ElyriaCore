from abc import ABC, abstractmethod
from typing import List
from domain.patient import Patient

class PatientRepository(ABC):
    @abstractmethod
    def add_patient(self, patient: Patient):
        pass

    @abstractmethod
    def get_patient(self, patient_id: int) -> Patient:
        pass

    @abstractmethod
    def update_patient(self, patient_id: int, patient: Patient):
        pass

    @abstractmethod
    def delete_patient(self, patient_id: int):
        pass

    @abstractmethod
    def get_all_patients(self) -> List[Patient]:
        pass

class PatientRepositoryImpl(PatientRepository):
    def __init__(self, database):
        self.database = database

    def add_patient(self, patient: Patient):
        self.database.create_patient(patient.to_dict())

    def get_patient(self, patient_id: int) -> Patient:
        patient_data = self.database.get_patient(patient_id)
        return Patient(**patient_data)

    def update_patient(self, patient_id: int, patient: Patient):
        self.database.update_patient(patient_id, patient.to_dict())

    def delete_patient(self, patient_id: int):
        self.database.delete_patient(patient_id)

    def get_all_patients(self) -> List[Patient]:
        patients_data = self.database.get_all_patients()
        return [Patient(**patient_data) for patient_data in patients_data]
