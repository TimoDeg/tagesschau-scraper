from pathlib import Path

# Base directory (this file is in src/)
SRC_DIR = Path(__file__).parent
DATA_DIR = SRC_DIR / "data"

# File paths (using consistent naming)
RAW_NEWS_PATH = DATA_DIR / "raw" / "news.jsonl"
PROCESSED_DATA_PATH = DATA_DIR / "processed" / "data.txt"
COMMON_WORDS_PATH = DATA_DIR / "processed" / "common_words.jsonl"

# Create directories if needed
DATA_DIR.mkdir(parents=True, exist_ok=True)
(DATA_DIR / "raw").mkdir(exist_ok=True)
(DATA_DIR / "processed").mkdir(exist_ok=True)