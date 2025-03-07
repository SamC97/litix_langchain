from pdf2image import convert_from_path

def pdf_to_images(pdf_path: str, dpi: int = 300):
    """
    Convert a PDF file into a list of images (one image per page).

    Parameters:
        pdf_path (str): Path to the PDF file.
        dpi (int): Resolution used for the conversion (default 300 dpi).

    Returns:
        List[PIL.Image.Image]: List of images.
    """
    images = convert_from_path(pdf_path, dpi=dpi)
    return images