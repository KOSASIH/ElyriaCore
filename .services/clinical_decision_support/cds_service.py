from typing import List
from patient_entity import Patient

class CDSService:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def get_rules(self):
        return self.rules

    def evaluate_rules(self, patient: Patient):
        results = []
        for rule in self.rules:
            result = rule.evaluate(patient)
            results.append(result)
        return results

    def get_recommendations(self, patient: Patient):
        recommendations = []
        for result in self.evaluate_rules(patient):
            if result:
                recommendations.append(result.recommendation)
        return recommendations

    def save_recommendations(self, patient: Patient, recommendations):
        # Implement saving logic here
        pass

    def load_recommendations(self, patient: Patient):
        # Implement loading logic here
        pass
