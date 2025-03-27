def test_chat_returns_response(test_client):

    """
    Test that the /chat endpoint responds correctly to a basic user message.

    This test sends a simple "Hi" message to the chatbot endpoint
    and verifies that:
    - The response returns a 200 status code.
    - The response contains a "response" key in the returned JSON.

    Args:
        test_client (TestClient): The FastAPI test client fixture.
    """

    payload = {"message": "Hi"}
    response = test_client.post("/chat", json=payload)
    assert response.status_code == 200
    assert "response" in response.json()

def test_clear_chat(test_client):
    """
    Test the /clear-chat endpoint to ensure it clears
    in-memory conversation history and returns success message.
    """
    response = test_client.post("/clear-chat")
    assert response.status_code == 200
    assert response.json()["message"] == "Chat history cleared."