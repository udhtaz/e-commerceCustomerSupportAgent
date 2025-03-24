def test_home_page_loads(test_client):

    """
    Test that the homepage ("/") loads successfully and returns HTML content.

    This test ensures:
    - The homepage endpoint returns a 200 OK status.
    - The content type of the response is HTML.

    Args:
        test_client (TestClient): The FastAPI test client fixture.
    """

    response = test_client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
