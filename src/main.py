import sys
import subprocess
from pathlib import Path
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

# Set up paths
BASE_DIR = Path(__file__).parent
sys.path.insert(0, str(BASE_DIR.parent))

# Import modules
from src.paths import DATA_DIR
from src.analyzer.common_words import filter_words
from src.data.processor import process_words
from src.ui.mainUi import display_data
from src.scraper.tagesschau import Tagesschau

def run_scrapy_spider():
    """Run Scrapy spider and return success status"""
    try:
        process = CrawlerProcess(get_project_settings())
        process.crawl(Tagesschau)
        process.start()
        return True
    except Exception as e:
        print(f"Scrapy error: {e}")
        return False

def run_data_processing():
    """Process data and return success status"""
    try:
        print("Processing scraped data...")
        process_words()
        filter_words()
        return True
    except Exception as e:
        print(f"Data processing error: {e}")
        return False

def run_streamlit_ui():
    """Run Streamlit UI with proper handling"""
    try:
        ui_path = str(BASE_DIR / "ui" / "mainUi.py")
        process = subprocess.Popen(["streamlit", "run", ui_path])
        return process
    except Exception as e:
        print(f"Streamlit error: {e}")
        return None

def main():
    print("Starting NewsScraper application...")
    
    streamlit_process = None
    
    try:
        if "--full" in sys.argv:
            if run_scrapy_spider() and run_data_processing():
                streamlit_process = run_streamlit_ui()
        elif "--process" in sys.argv:
            run_data_processing()
        elif "--ui" in sys.argv:
            streamlit_process = run_streamlit_ui()
        else:
            if run_data_processing():
                streamlit_process = run_streamlit_ui()
        
        if streamlit_process:
            streamlit_process.wait()
            
    except KeyboardInterrupt:
        print("\nShutting down gracefully...")
        if streamlit_process:
            streamlit_process.terminate()
    except Exception as e:
        print(f"Application error: {e}")
        if streamlit_process:
            streamlit_process.terminate()
        sys.exit(1)

if __name__ == "__main__":
    main()