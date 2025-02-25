# src/nlu/entity_extractor.py
import re

class EntityExtractor:
    def __init__(self):
        pass

    def extract_entities(self, message):
        """Extracts entities from the message."""
        medication = self.extract_medication_name(message)
        entities = {"medication": medication}
        return entities

    def extract_medication_name(self, message):
        """Extracts medication name from the message using regex"""
        medication_match = re.search(r"(amoxicillin|lisinopril|atorvastatin|cina pM Tmg Cap)", message, re.IGNORECASE)
        if medication_match:
            return medication_match.group(1)
        return None
