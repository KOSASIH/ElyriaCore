from typing import List
from domain.medical_record import MedicalRecord

class MedicalRecordService:
    def __init__(self):
        self.medical_records = []

    def add_medical_record(self, medical_record: MedicalRecord):
        self.medical_records.append(medical_record)

    def get_medical_record(self, medical_record_id: int) -> MedicalRecord:
        for medical_record in self.medical_records:
            if medical_record.id == medical_record_id:
                return medical_record
        return None

    def update_medical_record(self, medical_record_id: int, medical_record: MedicalRecord):
        for i, existing_medical_record in enumerate(self.medical_records):
            if existing_medical_record.id == medical_record_id:
                self.medical_records[i] = medical_record
                break

    def delete_medical_record(self, medical_record_id: int):
        for i, medical_record in enumerate(self.medical_records):
            if medical_record.id == medical_record_id:
                del self.medical_records[i]
                break

    def get_all_medical_records(self) -> List[MedicalRecord]:
        return self.medical_records

    def create_diagnosis(self, medical_record_id: int, diagnosis: str):
        medical_record = self.get_medical_record(medical_record_id)
        if medical_record:
            medical_record.diagnoses.append(diagnosis)
            return diagnosis
        else:
            return None

    def get_diagnosis(self, medical_record_id: int, diagnosis_id: int) -> str:
        medical_record = self.get_medical_record(medical_record_id)
        if medical_record:
            for diagnosis in medical_record.diagnoses:
                if diagnosis.id == diagnosis_id:
                    return diagnosis
        return None

    def update_diagnosis(self, medical_record_id: int, diagnosis_id: int, diagnosis: str):
        medical_record = self.get_medical_record(medical_record_id)
        if medical_record:
            for i, existing_diagnosis in enumerate(medical_record.diagnoses):
                if existing_diagnosis.id == diagnosis_id:
                    medical_record.diagnoses[i] = diagnosis
                    break
        return None

    def delete_diagnosis(self, medical_record_id: int, diagnosis_id: int):
        medical_record = self.get_medical_record(medical_record_id)
        if medical_record:
            for i, diagnosis in enumerate(medical_record.diagnoses):
                if diagnosis.id == diagnosis_id:
                    del medical_record.diagnoses[i]
                    break
        return None
