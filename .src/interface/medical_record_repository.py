from abc import ABC, abstractmethod
from typing import List
from domain.medical_record import MedicalRecord

class MedicalRecordRepository(ABC):
    @abstractmethod
    def add_medical_record(self, medical_record: MedicalRecord):
        pass

    @abstractmethod
    def get_medical_record(self, medical_record_id: int) -> MedicalRecord:
        pass

    @abstractmethod
    def update_medical_record(self, medical_record_id: int, medical_record: MedicalRecord):
        pass

    @abstractmethod
    def delete_medical_record(self, medical_record_id: int):
        pass

    @abstractmethod
    def get_all_medical_records(self) -> List[MedicalRecord]:
        pass

class MedicalRecordRepositoryImpl(MedicalRecordRepository):
    def __init__(self, database):
        self.database = database

    def add_medical_record(self, medical_record: MedicalRecord):
        self.database.create_medical_record(medical_record.to_dict())

    def get_medical_record(self, medical_record_id: int) -> MedicalRecord:
        medical_record_data = self.database.get_medical_record(medical_record_id)
        return MedicalRecord(**medical_record_data)

    def update_medical_record(self, medical_record_id: int, medical_record: MedicalRecord):
        self.database.update_medical_record(medical_record_id, medical_record.to_dict())

    def delete_medical_record(self, medical_record_id: int):
        self.database.delete_medical_record(medical_record_id)

    def get_all_medical_records(self) -> List[MedicalRecord]:
        medical_records_data = self.database.get_all_medical_records()
        return [MedicalRecord(**medical_record_data) for medical_record_data in medical_records_data]
