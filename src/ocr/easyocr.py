import numpy as np
import easyocr
from PIL import Image
from .base import OCRBase
from src.utils.text_utils import reconstruct_lines_easyocr

class EasyOCR(OCRBase):
    def __init__(self, lang_list: list = ['en']):
        self.reader = easyocr.Reader(lang_list, download_enabled=True)

    def ocr(self, image: Image.Image) -> str:
        result = self.reader.readtext(
            np.array(image),
            detail=1,        # Retourne les informations détaillées
            paragraph=False, # Optionnel selon ton besoin
            slope_ths=0.2,
            ycenter_ths=0.5,
            height_ths=0.5,
            width_ths=0.5,
            mag_ratio=1.0
        )
        return reconstruct_lines_easyocr(result)