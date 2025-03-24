from sqlalchemy import Column, String
from app.infrastructure.db.base import Base


class Order(Base):

    """
    SQLAlchemy model representing an e-commerce order.

    Attributes:
        order_id (str): Unique identifier for the order.
        item (str): Name or description of the item purchased.
        purchase_date (str): Date when the item was purchased.
        status (str): Current status of the order (e.g., 'Shipped', 'Delivered').
        shipped_date (str): Date the item was shipped.
        delivery_date (str): Date the item was delivered to the customer.
        payment_method (str): Method of payment used (e.g., 'Credit Card', 'PayPal').
        return_policy (str): Return eligibility of the item (e.g., 'Returnable', 'Non-returnable').
    """

    __tablename__ = "orders"

    order_id = Column(String, primary_key=True, index=True)
    item = Column(String)
    purchase_date = Column(String)
    status = Column(String)
    shipped_date = Column(String)
    delivery_date = Column(String)
    payment_method = Column(String)
    return_policy = Column(String)
