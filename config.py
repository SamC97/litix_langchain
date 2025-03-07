from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    """
    Settings class that contains configuration variables for the application.
    
    Attributes:
        QWEN2_5_7B (str): The path to the QWEN2_5_7B model.
        PHI4 (str): The path to the PHI4 model.
        CONTEXT_SIZE (int): The context size to use for the Ollama model.
        OLLAMA_GEN_URL (str): The URL for the Ollama generation model.
        OLLAMA_EMB_URL (str): The URL for the Ollama embedding model.
        OLLAMA_PULL_URL (str): The URL for the Ollama pull model.
    """

    # Model configuration variables
    QWEN2_5_7B: str
    PHI4: str
    CONTEXT_SIZE: int
        
    # Ollama configuration
    OLLAMA_GEN_URL: str
    OLLAMA_EMB_URL: str
    OLLAMA_PULL_URL: str

    class Config:
        """
        Pydantic configuration class for the Settings model.
        
        Attributes:
            env_file (str): The name of the environment file to load variables from.
            extra (str): Specify how to handle extra fields in the model.
        """
        env_file = ".env"
        extra = "allow"

# Instantiate the settings object
settings = Settings()