# src/nlu/intent_classifier.py
import re

class IntentClassifier:
    def __init__(self):
        pass

    def classify_intent(self, message):
        """Classifies the intent of the message."""
        message = message.lower()

        if "refill" in message:
            return "refill_medication"
        elif "dosage" in message:
            return "check_dosage"
        elif "hello" in message or "hi" in message:
            return "greeting"
        else:
            return "unknown"
