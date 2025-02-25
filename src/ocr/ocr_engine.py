# src/ocr/ocr_engine.py
from abc import ABC, abstractmethod
from paddleocr import PaddleOCR

class OCROptions:
    def __init__(self, use_angle_cls=True, lang='en'):
        self.use_angle_cls = use_angle_cls
        self.lang = lang

class OCREngine(ABC):
    @abstractmethod
    def extract_text(self, image_path):
        pass

class PaddleOCREngine(OCREngine):
    def __init__(self, options:OCROptions):
        self.ocr_engine = PaddleOCR(use_angle_cls=options.use_angle_cls, lang=options.lang)

    def extract_text(self, image_path):
        """Extracts text from a prescription image using OCR."""
        result = self.ocr_engine.ocr(image_path, cls=True)
        text = ""
        for line in result:
            for word_info in line:
                if isinstance(word_info, list) and len(word_info) > 1:
                    text += word_info[1][0] + "\n"
        return text

class OCRFactory:
    @staticmethod
    def create_ocr_engine(options:OCROptions):
        return PaddleOCREngine(options)
