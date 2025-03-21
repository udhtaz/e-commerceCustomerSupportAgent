import sqlite3
from langchain.tools import BaseTool

class OrderStatusTool(BaseTool):
    name: str = "order_status_tool"
    description: str = (
        "Use this to get the status of an order. "
        "Input should be the order ID as a string. "
        "Output is a string with the current status of that order."
    )

    def _run(self, order_id: str) -> str:
        if not order_id.strip():
            return "Please provide a valid order ID."

        try:
            conn = sqlite3.connect("data/orders.db")
            cursor = conn.cursor()
            cursor.execute("SELECT status FROM orders WHERE order_id = ?", (order_id,))
            result = cursor.fetchone()
            conn.close()

            if result:
                return f"Order {order_id} is currently {result[0]}."
            else:
                return f"Order {order_id} not found. Please check your order ID."
        except Exception as e:
            return f"Error checking order status: {str(e)}"

    async def _arun(self, order_id: str) -> str:
        raise NotImplementedError("This tool does not support async.")