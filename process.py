from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

max_len = 500
# step 1: Tokenizer set up
with open(r"tokenizer.pickle_v3", "rb") as f:
    tokenizer = pickle.load(f)

def process_text(text, tokenizer =tokenizer, max_len=max_len):
    """
    Processes the input text by tokenizing and padding it.
    
    Args:
        text (str): The input text to process.
        tokenizer (Tokenizer): The Keras Tokenizer instance.
        max_len (int): The maximum length for padding sequences.
        
    Returns:
        np.ndarray: The padded sequence of tokens.
    """
    # Tokenize the text
    sequence = tokenizer.texts_to_sequences([text])
    
    # Pad the sequence
    padded_sequence = pad_sequences(sequence, maxlen=max_len, padding='post', truncating='post')
    
    return padded_sequence

__all__ = ['process_text', 'tokenizer']




