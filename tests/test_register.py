def test_register_user(client):
    payload = {
        "name": "John Doe",
        "email": "register_test@example.com",
        "password": "secret123"
    }
    
    response = client.post("/register", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "register_test@example.com"

