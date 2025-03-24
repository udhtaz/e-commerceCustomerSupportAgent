import sqlite3
from fastapi import APIRouter

orders_router = APIRouter(tags=["Orders"])

@orders_router.get("/orders", summary="View all orders", description="Returns all rows in the orders database.")
def get_all_orders():

    """
    Fetches and returns all records from the orders database.

    This endpoint connects to the SQLite database and retrieves all orders,
    including fields like order ID, item name, status, delivery dates, and return policy.
    It transforms the result into a list of dictionaries for JSON compatibility.

    Returns:
        list[dict]: A list of all orders, with each order represented as a dictionary
        mapping column names to values.
    """

    conn = sqlite3.connect("data/orders.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM orders")
    rows = cursor.fetchall()

    column_names = [description[0] for description in cursor.description]
    conn.close()

    return [dict(zip(column_names, row)) for row in rows]