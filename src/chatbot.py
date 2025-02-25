import re
from src.nlu.intent_classifier import IntentClassifier  # Import NLU components
from src.nlu.entity_extractor import EntityExtractor
from src.knowledge_base.knowledge_base import KnowledgeBase  # Import KnowledgeBase
from src.ocr.ocr_engine import OCROptions, OCRFactory

class PharmacistChatbot:
    def __init__(self,ocr_options:OCROptions = OCROptions()):
        # Initialize NLU components
        self.intent_classifier = IntentClassifier()
        self.entity_extractor = EntityExtractor()

        # Initialize knowledge base
        self.knowledge_base = KnowledgeBase()

        #Initialize OCR Engine
        self.ocr_engine = OCRFactory.create_ocr_engine(ocr_options)

    def process_message(self, message):
        """Processes user input and generates a response."""

        # 1. NLU: Intent Recognition and Entity Extraction
        intent, entities = self.understand_intent(message)

        # 2. Dialog Management
        response = self.generate_response(intent, entities)

        return response

    def understand_intent(self, message):
        """Uses NLU to understand the user's intent and extract entities."""
        intent = self.intent_classifier.classify_intent(message)
        entities = self.entity_extractor.extract_entities(message)
        return intent, entities

    def generate_response(self, intent, entities):
        """Generates a response based on the intent and entities."""
        if intent == "refill_medication":
            medication = entities.get("medication")
            if medication:
                # Check if medication is in stock
                if self.knowledge_base.is_medication_in_stock(medication):
                    return f"Okay, refilling your {medication}. Please confirm your address."
                else:
                    return f"Sorry, {medication} is not currently in stock. Please contact the pharmacy."
            else:
                return "Which medication would you like to refill?"

        elif intent == "check_dosage":
            medication = entities.get("medication")
            if medication:
                dosage = self.knowledge_base.get_medication_dosage(medication)
                if dosage:
                    return f"The typical dosage for {medication} is {dosage}. Please consult with your doctor."
                else:
                    return f"Sorry, I don't have dosage information for {medication}."
            else:
                return "Which medication are you asking about?"
        elif intent == "greeting":
            return "Hello! How can I assist you today?"
        else:
            return "I'm sorry, I didn't understand. How can I help?"

    def process_image(self, image_path):
        """Extracts text from a prescription image using OCR."""
        text = self.ocr_engine.extract_text(image_path)
        return text
