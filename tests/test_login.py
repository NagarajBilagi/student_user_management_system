def test_login_user(client):
    # First register user
    client.post("/register", json={
        "name": "John",
        "email": "login_test@example.com",
        "password": "pass123"
    })
    
    # Login
    response = client.post("/login", json={
        "email": "login_test@example.com",
        "password": "pass123"
    })

    assert response.status_code == 200
    assert "access_token" in response.json()
