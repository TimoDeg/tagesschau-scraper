import json
from pathlib import Path
from src.paths import RAW_NEWS_PATH, PROCESSED_DATA_PATH  # Use the new names

def process_words():
    try:
        with open(RAW_NEWS_PATH, "r", encoding="utf-8") as infile, \
             open(PROCESSED_DATA_PATH, "w", encoding="utf-8") as outfile:
            
            for line in infile:
                data = json.loads(line.strip())
                title = data.get("title", "")
                description = data.get("description", "")
                
                if title or description:
                    outfile.write(f"{title}. {description}; ")
                    
    except Exception as e:
        print(f"Processing error: {e}")
        raise