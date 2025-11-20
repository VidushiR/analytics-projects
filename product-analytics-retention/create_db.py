import pandas as pd
import sqlite3
from pathlib import Path

# Paths
#RAW_PATH = Path("data/raw/events.csv")
RAW_PATH = Path("data/raw/product.csv")   
DB_PATH = Path("data/processed/analytics.db")

DB_PATH.parent.mkdir(parents=True, exist_ok=True)

print("Loading CSV...")
df = pd.read_csv(RAW_PATH)

print("Shape:", df.shape)
print(df.dtypes)

# Optional: rename columns if needed to match schema
# df.rename(columns={"old": "new"}, inplace=True)

print("Writing to SQLite...")
conn = sqlite3.connect(DB_PATH)
df.to_sql("events", conn, if_exists="replace", index=False)
conn.close()

print("Done! Wrote to", DB_PATH)
