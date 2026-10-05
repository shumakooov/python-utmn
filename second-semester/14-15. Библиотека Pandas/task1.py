# img/2.14-15.1.png
import pandas as pd

def length_stats(text):
    text = text.lower()
    clear_text = ''

    punctuation = "!?\":;-.,0123456789"
    for char in text:
        if char not in punctuation:
            clear_text += char
    
    words = list(set(clear_text.split()))
    
    words.sort()
    
    return pd.Series([len(word) for word in words], index=words)

