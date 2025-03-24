import streamlit as st
import pandas as pd
import json
from pathlib import Path
import datetime

def display_data():
    try:
        # CORRECT PATH - points to src/data/processed
        current_dir = Path(__file__).parent
        data_path = current_dir.parent / "data" / "processed" / "common_words.jsonl"
        
        st.write(f"Most used words at Tagesschau on the {datetime.date.today()}")
        
        if not data_path.exists():
            st.error(f"Data file not found at: {data_path}")
            st.error("Please run the data processing first (python -m src.main --process)")
            return

        data = []
        with open(data_path, "r", encoding="utf-8") as f:
            for line in f:
                data.append(json.loads(line))
        
        if data:
            df = pd.DataFrame(data)
            st.dataframe(df.sort_values("frequency", ascending=False).head(50))
        else:
            st.warning("No data found in the file")

    except Exception as e:
        st.error(f"Error loading data: {str(e)}")

def main():
    st.title("News Analyzer Dashboard")
    display_data()

if __name__ == "__main__":
    main()