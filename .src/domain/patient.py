from dataclasses import dataclass
from typing import Optional, List

@dataclass
class Patient:
    id: int
    name: str
    date_of_birth: str
    address: str
    phone_number: str
    email: str
    medical_history: Optional[List[str]] = None
    medications: Optional[List[str]] = None
    allergies: Optional[List[str]] = None

    def __post_init__(self):
        if self.medical_history is None:
            self.medical_history = []
        if self.medications is None:
            self.medications = []
        if self.allergies is None:
            self.allergies = []

    def add_medical_history(self, medical_history: str):
        self.medical_history.append(medical_history)

    def add_medication(self, medication: str):
        self.medications.append(medication)

    def add_allergy(self, allergy: str):
        self.allergies.append(allergy)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "date_of_birth": self.date_of_birth,
            "address": self.address,
            "phone_number": self.phone_number,
            "email": self.email,
            "medical_history": self.medical_history,
            "medications": self.medications,
            "allergies": self.allergies
        }
