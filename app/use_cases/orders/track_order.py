from app.infrastructure.repositories.order_repository import OrderRepository

class TrackOrderUseCase:

    """
    Use case for tracking the status of a specific order.

    This class encapsulates the logic needed to retrieve an order's status
    by interacting with the order repository.
    """

    def __init__(self, repository: OrderRepository):

        """
        Initialize the use case with a repository instance.

        Args:
            repository (OrderRepository): The repository used to access order data.
        """

        self.repository = repository

    def execute(self, order_id: str) -> str:


        """
        Retrieves the status of an order by its ID.

        Args:
            order_id (str): The unique identifier of the order.

        Returns:
            str: A message with the order status, or a not found message.
        
        Example:
            >>> use_case = TrackOrderUseCase(order_repository)
            >>> use_case.execute("12345")
            "Order 12345 is currently In Transit."
        """
        
        return self.repository.get_status(order_id)
