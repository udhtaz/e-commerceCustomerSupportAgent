def test_get_all_orders(test_client):

    """
    Test that the /orders endpoint returns a list of orders.

    This test sends a GET request to the /orders endpoint and verifies:
    - The response has a 200 OK status.
    - The response body is a list, representing order records.

    Args:
        test_client (TestClient): The FastAPI test client fixture.
    """

    response = test_client.get("/orders")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
