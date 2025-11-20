# User Retention & Engagement Dashboard

This project analyzes user behavior and retention using the **"How to Do Product Analytics"** dataset from Kaggle and builds an interactive dashboard to visualize key product metrics like DAU, WAU, MAU, retention, and churn.

## Project Structure

- `data/raw/` – original CSV files from Kaggle  
- `data/processed/` – cleaned data and SQLite database (`analytics.db`)  
- `notebooks/` – Jupyter notebooks for EDA, cohort analysis, and metrics  
- `sql/` – SQL scripts to define tables and views  
- `reports/` – final PDF report and presentation slides  

## Setup

```bash
# create and activate virtual environment (Windows)
python -m venv .venv
.\.venv\Scripts\activate

# install dependencies
pip install -r requirements.txt
