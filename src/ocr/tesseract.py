import pytesseract
from PIL import Image
from .base import OCRBase

class TesseractOCR(OCRBase):
    def __init__(self, lang: str = 'eng'):
        self.lang = lang

    def ocr(self, image: Image.Image) -> str:
        return pytesseract.image_to_string(image, lang=self.lang)