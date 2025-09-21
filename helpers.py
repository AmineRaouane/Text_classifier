from typing import Annotated, Tuple, List
from tensorflow.keras.preprocessing.sequence import pad_sequences
import logging

from config import MAX_SEQUENCE_LENGTH

logger = logging.getLogger(__name__)

def predict(
    text: str,
    model,
    tokenizer
) -> Tuple[
    Annotated[int, "prediction"],
    Annotated[float, "probability"]
]:
    """
    Make a prediction on the input text.

    Args:
        text: Input text to classify
        model: Loaded Keras model
        tokenizer: Loaded tokenizer

    Returns:
        Tuple of (prediction, probability)
    """
    try:
        sequences = tokenizer.texts_to_sequences([text])
        X = pad_sequences(sequences, maxlen=MAX_SEQUENCE_LENGTH, padding="post")
        preds = model.predict(X, verbose=0)
        bin_preds = (preds.ravel() >= 0.5).astype(int)
        return int(bin_preds[0]), float(preds.ravel()[0])

    except Exception as e:
        logger.error(f"Error in prediction: {e}")
        raise

def predict_batch(
    texts: List[str],
    model,
    tokenizer
) -> List[Tuple[
    Annotated[int, "prediction"],
    Annotated[float, "probability"]
]]:
    """
    Make predictions on a batch of input texts.

    Args:
        texts: List of input texts to classify
        model: Loaded Keras model
        tokenizer: Loaded tokenizer

    Returns:
        List of tuples (prediction, probability) for each text
    """
    try:
        if not texts:
            return []

        sequences = tokenizer.texts_to_sequences(texts)
        X = pad_sequences(sequences, maxlen=MAX_SEQUENCE_LENGTH, padding="post")
        preds = model.predict(X, verbose=0)
        bin_preds = (preds.ravel() >= 0.5).astype(int)
        results = []
        for i in range(len(texts)):
            results.append((int(bin_preds[i]), float(preds.ravel()[i])))

        return results

    except Exception as e:
        logger.error(f"Error in batch prediction: {e}")
        raise
