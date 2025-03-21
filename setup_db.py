import sqlite3

# Connect to SQLite (creates a new database file if it doesn't exist)
conn = sqlite3.connect("data/orders.db")
cursor = conn.cursor()

# Create orders table
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id TEXT PRIMARY KEY,
    status TEXT
)
""")

# Insert sample data
sample_orders = [
    ("12345", "Shipped"),
    ("67890", "In Transit"),
    ("11121", "Delivered"),
    ("12945", "Shipped"),
    ("63490", "Shipped"),
    ("14121", "Delivered")
]

cursor.executemany("INSERT OR IGNORE INTO orders (order_id, status) VALUES (?, ?)", sample_orders)

# Commit and close
conn.commit()
conn.close()

print("Database setup complete. Sample orders inserted.")
