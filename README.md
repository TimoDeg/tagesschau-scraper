# 📰 NewsScraper Project

A Python application that scrapes news articles, processes the text, and displays word frequency analysis in a Streamlit dashboard.
This project is for learning purposes and is not complete.

## 🏗️ Project Structure

```
NewsScraper/
├── src/
│   ├── analyzer/          # Text analysis components
│   ├── data/              # Data processing scripts
│   ├── scraper/           # Web scraping components
│   ├── ui/                # Streamlit dashboard
│   ├── paths.py           # Centralized path configuration
│   └── main.py            # Main application entry point
├── data/                  # Processed data files
│   ├── raw/               # Raw scraped articles
│   └── processed/         # Analyzed word frequencies
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/NewsScraper.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download NLTK data:
   ```python
   python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
   ```

## 🚀 Usage

Run different components using these commands:

| Command | Description |
|---------|-------------|
| `python -m src.main --full` | Run full pipeline (scrape + process + display) |
| `python -m src.main --process` | Just scrape and process data |
| `python -m src.main --ui` | Just launch the dashboard |
| `python -m src.main` | Default: process data + display dashboard |

The Streamlit dashboard will open automatically in your browser at `http://localhost:8501`

## 🔧 Components

1. **Scraper**: Collects news articles from Tagesschau RSS feed
2. **Processor**: Cleans and prepares the text data
3. **Analyzer**: Calculates word frequencies
4. **Dashboard**: Interactive visualization of results
