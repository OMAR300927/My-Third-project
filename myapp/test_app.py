import pytest
from flask_app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home_unauthenticated(client):
    response = client.get("/")
    assert response.status_code == 401
    assert b"You are not logged in" in response.data

def test_login_logout_flow(client):
    # تسجيل الدخول
    response = client.post("/login", json={
        "username": "admin",
        "password": "admin123"
    })
    assert response.status_code == 200
    assert b"Login successful!" in response.data

    # التحقق من صفحة home بعد تسجيل الدخول
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome admin!" in response.data

    # تسجيل الخروج
    response = client.post("/logout")
    assert response.status_code == 200
    assert b"Logged out" in response.data
