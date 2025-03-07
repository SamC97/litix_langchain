import re
import os

def crop_markdown_by_page(md_filepath: str, page_number: int, output_filepath: str = None) -> str:
    """
    Crop a Markdown file based on page break markers, and save the cropped version to a new file,
    without altering the original Markdown file.

    This function assumes that the Markdown file contains page break markers formatted as:
        "### PAGE_BREAK: <number> ###"
    (with optional surrounding whitespace and newlines).

    Parameters:
        md_filepath (str): Path to the input Markdown file.
        page_number (int): The page number (inclusive) up to which the content should be kept.
        output_filepath (str, optional): Path to save the cropped Markdown file.
            If not provided, a new file will be created in a directory called "crop_markdown"
            (relative to the project root).

    Returns:
        str: The path to the newly created cropped Markdown file.
    """
    # Read the entire content of the Markdown file
    with open(md_filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    # Split the content based on the page break markers.
    pages = re.split(r"\n\s*###\s*PAGE_BREAK:\s*\d+\s*###\s*\n", content)

    # Ensure the requested page number does not exceed the available pages
    if page_number > len(pages):
        page_number = len(pages)

    # Combine the pages from the beginning up to the specified page number.
    cropped_content = "\n\n".join(pages[:page_number])
    #print(f"Cropped content up to page {page_number}:\n{cropped_content}")

    # Determine the output file path without altering the original file.
    if output_filepath is None:
        project_root = os.path.abspath(os.path.join(os.path.dirname(md_filepath), ".."))
        output_dir = os.path.join(project_root, "data", "crop_markdown")
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate a new filename based on the original file's name, e.g., "document_cropped.md"
        base_filename = os.path.basename(md_filepath)
        name, ext = os.path.splitext(base_filename)
        new_filename = f"{name}_cropped{ext}"
        output_filepath = os.path.join(output_dir, new_filename)

    # Write the cropped content to the new file
    with open(output_filepath, 'w', encoding='utf-8') as file:
        file.write(cropped_content)

    return output_filepath


def clean_llm_response(response: str) -> str:
    """
    Cleans the LLM response by removing newline characters and extra whitespace,
    ensuring the output is in one line.
    
    Args:
        response (str): The raw response from the LLM.
        
    Returns:
        str: The cleaned response as a single line.
    """
    # Replace newline characters with a space
    cleaned = response.replace("\n", " ")
    # Normalize multiple spaces into a single space
    cleaned = " ".join(cleaned.split())
    return cleaned


def clean_text_value(text_value: str) -> str:
    """
    Clean text value before comparison by :
     - stripping whitespace
     - converting to lowercase
     - removing all double quotes (")

    Args:
        text_value (str): The text value to clean.
        
    Returns:
        str: The cleaned text value.
    """
    cleaned_value = text_value.strip().lower().replace('"', '')
    return cleaned_value


def reconstruct_lines_easyocr(result, line_threshold=10):
    """
    Reconstructs the lines from the result of EasyOCR.

    Parameters:
        result (list): The result of EasyOCR.
        line_threshold (int): The threshold for the distance between two lines.

    Returns:
        str: The reconstructed text
    """
    segments = []
    for (bbox, text, confidence) in result:
        ys = [point[1] for point in bbox]
        min_y = min(ys)
        segments.append((min_y, text))
    segments.sort(key=lambda x: x[0])
    lines = []
    current_line = []
    current_line_y = None
    for (y, txt) in segments:
        if current_line_y is None:
            current_line.append(txt)
            current_line_y = y
        else:
            if abs(y - current_line_y) <= line_threshold:
                current_line.append(txt)
            else:
                lines.append(' '.join(current_line))
                current_line = [txt]
            current_line_y = y
    if current_line:
        lines.append(' '.join(current_line))
    return "\n".join(lines)


def reconstruct_lines_paddleocr(paddle_result, line_threshold=10):
    """
    Reconstructs the lines from the result of PaddleOCR.
    
    Parameters:
        paddle_result (list): The result of PaddleOCR.
        line_threshold (int): The threshold for the distance between two lines. 
        
    Returns:
        str: The reconstructed text
    """
    segments = []
    for entry in paddle_result:
        bbox = entry[0]
        txt = entry[1][0]
        ys = [point[1] for point in bbox]
        min_y = min(ys)
        segments.append((min_y, txt))
    segments.sort(key=lambda x: x[0])
    lines = []
    current_line = []
    current_line_y = None
    for (y, txt) in segments:
        if current_line_y is None:
            current_line.append(txt)
            current_line_y = y
        else:
            if abs(y - current_line_y) <= line_threshold:
                current_line.append(txt)
            else:
                lines.append(' '.join(current_line))
                current_line = [txt]
            current_line_y = y
    if current_line:
        lines.append(' '.join(current_line))
    return "\n".join(lines)