from app.services.order_service import check_order_status
import pytest

class MockOrder:
    def __init__(self, status):
        self.status = status

@pytest.fixture
def mock_repo(monkeypatch):
    from app.infrastructure.repositories import order_repository

    def mock_get_order_by_id(self, order_id):
        return MockOrder("Delivered") if order_id == "10001" else None

    monkeypatch.setattr(order_repository.OrderRepository, "get_order_by_id", mock_get_order_by_id)

def test_check_order_status_existing(mock_repo):
    """
    Test that check_order_status returns correct message for existing order.
    """
    response = check_order_status("10001")
    assert "Order 10001 is currently Delivered" in response

def test_check_order_status_not_found(mock_repo):
    """
    Test that check_order_status returns error message for missing order.
    """
    response = check_order_status("99999")
    assert "Order 99999 not found" in response

