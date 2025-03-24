"""
Domain policy definitions for return policies.
"""

RETURN_POLICIES = {
    "general": (
        "You can return most items within 30 days of purchase for a full refund or exchange. "
        "Items must be in their original condition, with all tags and packaging intact. "
        "Please bring your receipt or proof of purchase when returning items."
    ),
    "exceptions": (
        "Certain items such as clearance merchandise, perishable goods, and personal care items are "
        "non-returnable. Please check the product description or ask a store associate for more details."
    ),
    "refunds": (
        "Refunds will be issued to the original form of payment. "
        "If you paid by credit card, the refund will be credited to your card. "
        "If you paid by cash or check, you will receive a cash refund."
    ),
}
