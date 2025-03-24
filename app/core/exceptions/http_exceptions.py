class AppException(Exception):

    """
    Base exception class for application-specific errors.

    All custom exceptions in the application should inherit from this class.
    """

    pass

class OrderNotFoundError(AppException):

    """
    Raised when an order with a specified ID is not found in the database.

    Args:
        order_id (str): The ID of the order that could not be found.
    """

    def __init__(self, order_id: str):
        super().__init__(f"Order with ID '{order_id}' not found.")

class InvalidOrderInput(AppException):

    """
    Raised when input provided for order-related actions is invalid.

    Args:
        reason (str): A description of why the input is considered invalid.
    """

    def __init__(self, reason: str):
        super().__init__(f"Invalid order input: {reason}")
