import re
from datetime import datetime

def search_year(text: str) -> str:
    """
    Extract the year of the document.
    The year must be a 4-digit number between 1950 and the current year.
    
    Args:
        text (str): The text to search in.
        
    Returns:
        str: The year found in the text, or an empty string if no year was found.
    """
    current_year = datetime.now().year
    # Generate a list of valid years as strings
    valid_years = [str(year) for year in range(1950, current_year + 1)]
    # Create a regex pattern to match any of the valid years
    pattern = r'\b(?:' + '|'.join(valid_years) + r')\b'
    
    match = re.search(pattern, text)
    return match.group(0) if match else "year not found"