# db_setup.py
import sqlite3
import logging
import random
from datetime import datetime, timedelta
import os

logging.basicConfig(level=logging.INFO)

def setup_database():
    os.makedirs("data", exist_ok=True) 
    conn = sqlite3.connect("data/orders.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        order_id TEXT PRIMARY KEY,
        item TEXT,
        purchase_date TEXT,
        status TEXT,
        shipped_date TEXT,
        delivery_date TEXT,
        payment_method TEXT,
        return_policy TEXT
    )
    """)

    returnable_items = [
        "Laptop", "Smartphone", "Headphones", "Tablet", "Camera",
        "Gaming Console", "Smartwatch", "TV", "Bluetooth Speaker",
        "External Hard Drive", "Keyboard", "Mouse", "Monitor", 
        "Printer", "Router", "Projector", "VR Headset", "Power Bank"
    ]

    non_returnable_items = [
        "Diapers", "Malt Drink", "Coffee Maker", "Washing Machine", "Toothbrush",
        "Toothpaste", "Deodorant", "Shaving Cream", "Vitamins", "Protein Powder",
        "Lipstick",  "Mascara", "Perfume", "Hair Dye", "Frozen Chicken", "Fresh Milk",
        "Yogurt", "Vegetables", "Shoes(Clearance)",  "Bags(Clearance)", "Shirts(Clearance)",
        "Sanitary Pads", "Insect Repellent", "Hand Sanitizer", "Face Mask"
    ]

    payment_methods = ["Cash", "Check", "Card"]
    statuses = ["Pending", "Shipped", "In Transit", "Delivered"]

    def random_date(start_days_ago=30, end_days_ago=1):
        if start_days_ago < end_days_ago:
            start_days_ago, end_days_ago = end_days_ago, start_days_ago
        random_days = random.randint(end_days_ago, start_days_ago)
        return (datetime.now() - timedelta(days=random_days)).strftime("%Y-%m-%d")

    sample_orders = []
    for i in range(30):
        order_id = str(10000 + i)
        item = random.choice(returnable_items + non_returnable_items)
        purchase_date = random_date(60, 20)
        status = random.choice(statuses)
        payment_method = random.choice(payment_methods)
        return_policy = "Returnable" if item in returnable_items else "Non-returnable"

        if status == "Shipped":
            shipped_date = random_date(10, 2)
            delivery_date = "N/A"
        elif status == "Delivered":
            shipped_date = random_date(15, 7)
            delivery_date = random_date(6, 1)
        else:
            shipped_date = "N/A"
            delivery_date = "N/A"

        sample_orders.append((order_id, item, purchase_date, status, shipped_date, delivery_date, payment_method, return_policy))

    cursor.executemany("""
    INSERT OR IGNORE INTO orders (order_id, item, purchase_date, status, shipped_date, delivery_date, payment_method, return_policy)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, sample_orders)

    conn.commit()
    conn.close()
    logging.info("📦 Database setup complete. 30 sample orders inserted.")