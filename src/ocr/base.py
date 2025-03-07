from abc import ABC, abstractmethod
from PIL import Image

class OCRBase(ABC):
    @abstractmethod
    def ocr(self, image: Image.Image) -> str:
        """
        Convert an image into text (or markdown).
        
        Parameters:
            image (PIL.Image.Image): Image to convert.
            
        Returns:
            str: Text extracted from the image.
        """
        pass