from dataclasses import dataclass
from typing import Optional, List
from patient import Patient

@dataclass
class MedicalRecord:
    id: int
    patient: Patient
    diagnoses: Optional[List[str]] = None
    treatments: Optional[List[str]] = None
    test_results: Optional[List[str]] = None

    def __post_init__(self):
        if self.diagnoses is None:
            self.diagnoses = []
        if self.treatments is None:
            self.treatments = []
        if self.test_results is None:
            self.test_results = []

    def add_diagnosis(self, diagnosis: str):
        self.diagnoses.append(diagnosis)

    def add_treatment(self, treatment: str):
        self.treatments.append(treatment)

    def add_test_result(self, test_result: str):
        self.test_results.append(test_result)

    def to_dict(self):
        return {
            "id": self.id,
            "patient": self.patient.to_dict(),
            "diagnoses": self.diagnoses,
            "treatments": self.treatments,
            "test_results": self.test_results
        }
