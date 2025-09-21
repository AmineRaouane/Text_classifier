import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Base directory
BASE_DIR = Path(__file__).resolve().parent

# Application settings
APP_NAME = os.getenv("APP_NAME", "Text Classification API")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# Server settings
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", 8000))
WORKERS = int(os.getenv("WORKERS", 1))

# Model settings
MAX_SEQUENCE_LENGTH = int(os.getenv("MAX_SEQUENCE_LENGTH", 50))
MODEL_PATH = BASE_DIR / os.getenv("MODEL_PATH", "model/model.h5")
TOKENIZER_PATH = BASE_DIR / os.getenv("TOKENIZER_PATH", "model/tokenizer.json")
