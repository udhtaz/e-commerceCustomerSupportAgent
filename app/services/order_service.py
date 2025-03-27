from app.infrastructure.repositories.order_repository import OrderRepository

def check_order_status(order_id: str) -> str:
    """
    Retrieves the status of an order from the repository.

    Args:
        order_id (str): The ID of the order.

    Returns:
        str: A message indicating the current status or an error.
    """
    repo = OrderRepository()
    order = repo.get_order_by_id(order_id)

    if order:
        return f"Order {order_id} is currently {order.status}."
    return f"Order {order_id} not found. Please check your order ID."