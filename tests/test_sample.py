# tests/test_api.py
import requests

def test_api_status():
    response = requests.get("https://openweathermap.org/api")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
