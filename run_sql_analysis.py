
from pathlib import Path
import sqlite3

ROOT = Path(__file__).resolve().parent
DB_PATH = ROOT / "data" / "customer_churn.db"
SQL_PATH = ROOT / "sql" / "churn_analysis.sql"

sql_text = SQL_PATH.read_text(encoding="utf-8")
sql_text = "\n".join(
    line for line in sql_text.splitlines()
    if not line.strip().startswith("--")
)

with sqlite3.connect(DB_PATH) as conn:
    conn.row_factory = sqlite3.Row

    for query in sql_text.split(";"):
        query = query.strip()
        if not query:
            continue

        print("\n" + "=" * 65)
        cursor = conn.execute(query)
        rows = cursor.fetchall()

        if rows:
            print(" | ".join(rows[0].keys()))
            for row in rows:
                print(" | ".join(str(value) for value in row))
