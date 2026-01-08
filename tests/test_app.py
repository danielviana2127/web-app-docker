import os
import requests
import pytest

BASE_URL = os.getenv("APP_BASE_URL", "http://localhost:8000")
TIMEOUT = 5


@pytest.mark.integration
def test_home():
    """Verifica se a rota raiz responde corretamente."""
    response = requests.get(f"{BASE_URL}/", timeout=TIMEOUT)
    assert response.status_code == 200


@pytest.mark.integration
def test_health():
    """Verifica se o endpoint de healthcheck está funcional."""
    response = requests.get(f"{BASE_URL}/health", timeout=TIMEOUT)
    assert response.status_code == 200

    data = response.json()
    assert "status" in data
    assert data["status"] == "ok"