from app.infrastructure.repositories.order_repository import OrderRepository

def test_get_order_by_id_found(monkeypatch):
    """
    Test that `get_order_by_id` returns a valid Order object
    when the order exists in the database.
    """
    repo = OrderRepository()

    def mock_connect(path):
        class Cursor:
            def execute(self, query, param): pass
            def fetchone(self): return ("10001", "John Doe", "Shipped", "Laptop", "Returnable")
            def close(self): pass
        class Conn:
            def cursor(self): return Cursor()
            def close(self): pass
        return Conn()

    monkeypatch.setattr("sqlite3.connect", mock_connect)
    order = repo.get_order_by_id("10001")
    assert order is not None
    assert order.order_id == "10001"

def test_get_order_by_id_not_found(monkeypatch):
    """
    Test that `get_order_by_id` returns None when the order
    does not exist in the database.
    """
    repo = OrderRepository()

    def mock_connect(path):
        class Cursor:
            def execute(self, query, param): pass
            def fetchone(self): return None
            def close(self): pass
        class Conn:
            def cursor(self): return Cursor()
            def close(self): pass
        return Conn()

    monkeypatch.setattr("sqlite3.connect", mock_connect)
    order = repo.get_order_by_id("99999")
    assert order is None
