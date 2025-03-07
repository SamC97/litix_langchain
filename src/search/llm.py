import requests
from src.prompts.search_prompts import en_search_prompts, de_search_prompts
from src.utils.text_utils import clean_llm_response
from config import settings

LANG_PROMPTS = {
    "en": en_search_prompts,
    "de": de_search_prompts,
}

def search_title(text: str, model: str, max_context_size: int, lang: str) -> str:
    """
    Extract the document title using the LLM.
    """
        
    if lang not in LANG_PROMPTS:
        print(f"Language {lang} is not supported. Please choose from 'en' or 'de'.")
    else:
        prompt = LANG_PROMPTS[lang]["search_title"]
        final_prompt = f"{prompt} \n\n\n Here is the document to analyze : \n {text}" 
    
    payload = {
        "prompt": final_prompt,
        "model": model,
        "stream": False,
        "options": {
            "temperature": 0.0,
            "num_ctx": max_context_size,
        }
    }
    
    try:
        response = requests.post(settings.OLLAMA_GEN_URL, json=payload)
        response.raise_for_status()
        result = response.json()
        title = clean_llm_response(result.get("response", ""))
        return title
    except Exception as e:
        return f"Error: {e}"


def search_author(text: str, model: str, max_context_size: int, lang: str) -> str:
    """
    Extract the document author name using the LLM.
    """
        
    if lang not in LANG_PROMPTS:
        print(f"Language {lang} is not supported. Please choose from 'en' or 'de'.")
    else:
        prompt = LANG_PROMPTS[lang]["search_author"]
        final_prompt = f"{prompt} \n\n\n Here is the document to analyze : \n {text}" 
    
    payload = {
        "prompt": final_prompt,
        "model": model,
        "stream": False,
        "options": {
            "temperature": 0.0,
            "num_ctx": max_context_size,
        }
    }
    
    try:
        response = requests.post(settings.OLLAMA_GEN_URL, json=payload)
        response.raise_for_status()
        result = response.json()
        author = clean_llm_response(result.get("response", ""))
        return author
    except Exception as e:
        return f"Error: {e}"
    
    
def search_if_groundwater_mentioned(text: str, model: str, max_context_size: int, lang: str) -> str:
    """
    Check if the text mentions groundwater using the LLM.
    """
    
    print(f"Text length: {len(text)}")
    
    # Check the text size (if it's too large, we need to split it into smaller parts and make multiple requests)
    if len(text) > 8192:
        print("Text is too large. Splitting into smaller parts.")
        
        is_groundwater_mentioned_in_part = False
        # Split the text into smaller parts
        text_parts = [text[i:i+8192] for i in range(0, len(text), 8192)]
        # Make a request for each part
        for i, part in enumerate(text_parts):
            print(f"Part {i+1} of {len(text_parts)}")
            is_groundwater_mentioned_in_part_str = search_if_groundwater_mentioned(part, model, max_context_size, lang)
            # check if "yes" is in the response to any of the parts and break if it is
            if "yes" in is_groundwater_mentioned_in_part_str.lower():
                is_groundwater_mentioned_in_part = True
                break
        return "yes" if is_groundwater_mentioned_in_part else "no"
            
    
    if lang not in LANG_PROMPTS:
        print(f"Language {lang} is not supported. Please choose from 'en' or 'de'.")
    else:
        prompt = LANG_PROMPTS[lang]["is_groundwater_mentioned"]
        final_prompt = f"{prompt} \n\n\n Here is the document to analyze : \n {text}" 
    
    payload = {
        "prompt": final_prompt,
        "model": model,
        "stream": False,
        "options": {
            "temperature": 0.0,
            "num_ctx": max_context_size,
        }
    }
    
    try:
        response = requests.post(settings.OLLAMA_GEN_URL, json=payload)
        response.raise_for_status()
        result = response.json()
        is_groundwater_mentioned = result.get("response", "")
        print(is_groundwater_mentioned)
        return is_groundwater_mentioned
    except Exception as e:
        return f"Error: {e}"
    
    
# unused function (replaced by separate functions above)    
def search(objective: str, text: str, model: str, max_context_size: int, lang: str) -> str:
    """
    Search for the requested information using the LLM.
    
    Args:
        objective (str): The information to search for.
        text (str): The context to search in.
        model (str): The model to use for the search.
        max_context_size (int): The maximum context size to use.
        lang (str): The language of the prompt to use.
        
    Returns:
        str: The extracted information.
    """
    
    # Select the appropriate prompt based on the objective and language
    # Dict of prompts for each language
    lang_prompts = {
        "en": en_search_prompts,
        "de": de_search_prompts,
    }

    # Dict of prompts for each objective
    objectives_prompts = {
        "title": "search_title",
        "author": "search_author",
        "is_groundwater_mentioned": "is_groundwater_mentioned",
    }

    if lang not in lang_prompts:
        print(f"Language {lang} is not supported. Please choose from 'en' or 'de'.")
    elif objective not in objectives_prompts:
        print(f"Objective {objective} is not supported. Please choose from 'title', 'author', or 'is_groundwater_mentioned'.")
    else:
        prompt = lang_prompts[lang][objectives_prompts[objective]]
        
    # Create the payload for the request
    payload = {
        "prompt": prompt,
        "context": text,
        "max_context_size": max_context_size,
        "model": model,
    }
    
    # Make a POST request to the Ollama generation model
    try:
        response = requests.post(settings.OLLAMA_GEN_URL, json=payload)
        response.raise_for_status()
        result = response.json()
        return result.get(objective, "")
    except Exception as e:  
        return f"Error: {e}"