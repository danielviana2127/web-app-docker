import requests

def test_home():
    r = requests.get("http://localhost:8000/")
    assert r.status_code == 200

def test_health():
    r = requests.get("http://localhost:8000/health")
    assert r.status_code == 200
    data = r.json()
    assert data["status"] == "ok"