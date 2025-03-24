def test_root_endpoint(test_client):

    """
    Test the root endpoint ("/") to ensure that the homepage loads successfully.

    This test checks:
    - The root URL is accessible.
    - It returns a 200 OK status, indicating successful rendering of the homepage.
    """

    response = test_client.get("/")
    assert response.status_code == 200
