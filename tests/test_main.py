from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "SkillPro Tech API is running!"}

def test_status():
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_process_data():
    data = {"name": "Test", "value": 123}
    response = client.post("/process", json=data)
    assert response.status_code == 200
    assert response.json() == {"processed_data": data}
