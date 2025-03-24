import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture(scope="module")
def test_client():

    """
    Fixture that provides a reusable TestClient instance for the FastAPI app.

    Scope is set to 'module' so it initializes once per test module,
    improving performance across multiple tests.
    
    Yields:
        TestClient: A test client instance to simulate API requests.
    """

    with TestClient(app) as client:
        yield client
