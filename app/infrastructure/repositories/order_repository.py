import sqlite3
from typing import Optional
from app.domain.order import Order

class OrderRepository:

    """
    Repository for accessing order data from the SQLite database.

    Attributes:
        DB_PATH (str): Path to the SQLite database file containing order information.
    """

    DB_PATH = "data/orders.db"

    def get_order_by_id(self, order_id: str) -> Optional[Order]:

        """
        Retrieve a single order by its ID.

        Args:
            order_id (str): The ID of the order to retrieve.

        Returns:
            Optional[Order]: The corresponding Order object if found, otherwise None.
        """

        conn = sqlite3.connect(self.DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders WHERE order_id = ?", (order_id,))
        row = cursor.fetchone()
        conn.close()

        if row:
            return Order(
                order_id=row[0],
                customer_name=row[1],
                status=row[2],
                item=row[3],
                return_policy=row[4]
            )
        return None
