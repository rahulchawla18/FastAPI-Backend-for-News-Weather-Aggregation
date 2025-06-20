def test_news_requires_auth(client):
    response = client.get("/news")
    assert response.status_code == 403

def test_news_with_auth(client):
    # Login first
    client.post("/signup", json={
        "email": "news@example.com",
        "password": "123456",
        "name": "News User"
    })
    login_res = client.post("/login", json={
        "email": "news@example.com",
        "password": "123456"
    })
    token = login_res.json()["access_token"]

    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/news?search=india&page=1&page_size=5", headers=headers)
    assert response.status_code == 200
    assert "articles" in response.json()
