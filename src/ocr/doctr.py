import os
import tempfile
from doctr.io import DocumentFile
from doctr.models import ocr_predictor
from .base import OCRBase
from PIL import Image

class DoctrOCR(OCRBase):
    def __init__(self, det_arch: str = "db_resnet50", reco_arch: str = "crnn_vgg16_bn", pretrained: bool = True):
        """
        Initialize the Doctr OCR engine with the specified detector and recognizer architectures.
        """
        self.model = ocr_predictor(det_arch=det_arch, reco_arch=reco_arch, pretrained=pretrained)
    
    def ocr(self, image: Image.Image) -> str:
        """
        Perform OCR on a single PIL image.
        
        Parameters:
            image (PIL.Image.Image): The image to convert.
        
        Returns:
            str: The concatenated text extracted from all pages.
        """
        # Ensure the image is in RGB mode.
        image = image.convert("RGB")
        # Save the image to a temporary file
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
            tmp_path = tmp.name
            image.save(tmp_path)
        
        try:
            # Pass the file path to DocumentFile.from_images
            doc = DocumentFile.from_images([tmp_path])
            result = self.model(doc)
            output_lines = []
            for page in result.pages:
                for block in page.blocks:
                    for line in block.lines:
                        line_text = " ".join(word.value for word in line.words)
                        output_lines.append(line_text)
            return "\n".join(output_lines)
        except Exception as e:
            print(f"Error during OCR with Doctr on {tmp_path}: {e}")
            return ""
        finally:
            # Clean up the temporary file
            os.remove(tmp_path)