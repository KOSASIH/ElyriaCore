from dataclasses import dataclass
from typing import Optional, List

@dataclass
class Study:
    id: int
    title: str
    description: str
    principal_investigator: str
    start_date: str
    end_date: str
    participants: Optional[List[str]] = None
    data: Optional[List[str]] = None
    results: Optional[List[str]] = None

    def __post_init__(self):
        if self.participants is None:
            self.participants = []
        if self.data is None:
            self.data = []
        if self.results is None:
            self.results = []

    def add_participant(self, participant: str):
        self.participants.append(participant)

    def add_data(self, data: str):
        self.data.append(data)

    def add_result(self, result: str):
        self.results.append(result)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "principal_investigator": self.principal_investigator,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "participants": self.participants,
            "data": self.data,
            "results": self.results
        }
