import pytest
import redis.asyncio as redis
import asyncio

@pytest.fixture(scope="module", autouse=True)
def skip_if_redis_unavailable():
    async def try_ping():
        try:
            r = redis.Redis(host="localhost", port=6379)
            await r.ping()
        except Exception:
            pytest.skip("Skipping weather tests: Redis not available.")

    asyncio.run(try_ping())

def test_weather_basic(client):
    response = client.get("/weather?city=Delhi")
    assert response.status_code == 200
    json_data = response.json()
    assert "data" in json_data
    assert "count" in json_data

def test_weather_pagination(client):
    response = client.get("/weather?city=Mumbai&page=2&page_size=5")
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["page"] == 2
    assert json_data["page_size"] == 5
    assert isinstance(json_data["data"], list)
