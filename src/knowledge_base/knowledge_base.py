# src/knowledge_base/knowledge_base.py
class KnowledgeBase:
    def __init__(self):
        # Mock database (same as before)
        self.mock_database = {
            "patients": {"12345": "John Doe", "67890": "Jane Smith"},
            "medications": ["Cina pM Tmg Cap", "Amoxicillin", "Lisinopril", "Atorvastatin"],  # Cina pm added to mock data
        }

    def is_medication_in_stock(self, medication):
        """Checks if the medication is in stock."""
        return medication.lower() in [m.lower() for m in self.mock_database["medications"]]

    def get_medication_dosage(self, medication):
        """Gets the dosage information for the medication."""
        # Replace this with your actual knowledge base lookup
        if medication.lower() == "amoxicillin":
            return "250mg three times a day"
        elif medication.lower() == "lisinopril":
            return "10mg once a day"
        else:
            return None
