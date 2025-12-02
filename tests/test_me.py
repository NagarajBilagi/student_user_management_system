def test_get_me_success(client):
    # 1. Register
    client.post("/register", json={
        "name": "Bob",
        "email": "me_test@example.com",
        "password": "123"
    })
    # 2. Login
    login = client.post("/login", json={
        "email": "me_test@example.com",
        "password": "123"
    }).json()
    
    token = login["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 3. Access /me
    response = client.get("/me", headers=headers)
    assert response.status_code == 200
    assert response.json()["email"] == "me_test@example.com"
