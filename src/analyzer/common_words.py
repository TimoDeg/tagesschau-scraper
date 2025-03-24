import json
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
from src.paths import PROCESSED_DATA_PATH, COMMON_WORDS_PATH  # Use new names

def filter_words():
    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True)
    
    german_stop_words = set(stopwords.words('german'))
    
    try:
        text_data = PROCESSED_DATA_PATH.read_text(encoding="utf-8")
        words = word_tokenize(text_data, language='german')
        filtered_words = [
            word.lower() for word in words 
            if word.isalpha() and word.lower() not in german_stop_words
        ]
        
        word_freq = Counter(filtered_words)
        
        with open(COMMON_WORDS_PATH, "w", encoding="utf-8") as file:
            for word, freq in word_freq.most_common():
                json.dump({"word": word, "frequency": freq}, file, ensure_ascii=False)
                file.write("\n")
                
    except Exception as e:
        print(f"Word filtering error: {e}")
        raise