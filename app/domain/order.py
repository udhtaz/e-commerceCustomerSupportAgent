from pydantic import BaseModel

class Order(BaseModel):

    """
    Schema representing a single e-commerce order record.

    Attributes:
        order_id (str): Unique identifier for the order.
        customer_name (str): Name of the customer who placed the order.
        status (str): Current status of the order (e.g., Shipped, Delivered).
        item (str): Name or description of the item ordered.
        return_policy (str): Return eligibility or policy related to the item.
    """

    order_id: str
    customer_name: str
    status: str
    item: str
    return_policy: str
