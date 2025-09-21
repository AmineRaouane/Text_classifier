from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import tokenizer_from_json
import logging

from config import MODEL_PATH, TOKENIZER_PATH

logger = logging.getLogger(__name__)

def load_model_and_tokenizer():
    """Load the trained model and tokenizer from disk."""
    try:
        logger.info(f"Loading model from: {MODEL_PATH}")
        model = load_model(MODEL_PATH)

        logger.info(f"Loading tokenizer from: {TOKENIZER_PATH}")
        with open(TOKENIZER_PATH, "r", encoding="utf-8") as f:
            tokenizer = tokenizer_from_json(f.read())

        logger.info("Model and tokenizer loaded successfully")
        return model, tokenizer

    except FileNotFoundError as e:
        logger.error(f"Model or tokenizer file not found: {e}")
        raise
    except Exception as e:
        logger.error(f"Error loading model or tokenizer: {e}")
        raise
