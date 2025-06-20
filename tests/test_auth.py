import uuid

def test_signup_and_login_flow(client):
    email = f"test_{uuid.uuid4().hex[:6]}@example.com"  # unique per test

    # Signup
    response = client.post("/signup", json={
        "email": email,
        "password": "secret123",
        "name": "Test User"
    })
    assert response.status_code == 200

    # Login
    response = client.post("/login", json={
        "email": email,
        "password": "secret123"
    })
    assert response.status_code == 200
    tokens = response.json()
    assert "access_token" in tokens
    assert "refresh_token" in tokens

    # Refresh
    response = client.post("/refresh", json={
        "refresh_token": tokens["refresh_token"]
    })
    assert response.status_code == 200
    assert "access_token" in response.json()

    # Logout
    headers = {"Authorization": f"Bearer {tokens['access_token']}"}
    response = client.post("/logout", headers=headers)
    assert response.status_code == 200
