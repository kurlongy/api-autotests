import requests
BASE_URL = "https://jsonplaceholder.typicode.com"
def test_users():
    response = requests.get(
        f"{BASE_URL}/users"
    )
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_user():
    response = requests.get(
        f"{BASE_URL}/users/1"
    )
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_user_not_found():
    response = requests.get(
    f"{BASE_URL}/users/999"
    )
    assert response.status_code == 404

def test_create_user():
    response = requests.post(
        f"{BASE_URL}/users",
        json = {
            "name": "QA Test",
            "username": "qa_test",
            "email": "qa@test.com"
        }
    )
    assert response.status_code == 201
    assert response.json()["name"] == "QA Test"
    assert response.json()["username"] == "qa_test"
    assert response.json()["email"] == "qa@test.com"

def test_delete_user():
    response = requests.delete(
        f"{BASE_URL}/users/1"
    )
    assert response.status_code == 200

def test_filter_users_by_id():
    response = requests.get(
        f"{BASE_URL}/users",
        params = {"id":1}
    )
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["id"] == 1

def test_filter_users_by_nonexistent_id():
    response = requests.get(
        f"{BASE_URL}/users",
        params = {"id":999}
    )
    assert response.status_code == 200
    assert len(response.json()) == 0

def test_create_user_without_email():
    response = requests.post(
        f"{BASE_URL}/users",
        json={
            "name":"QA Test",
            "username":"qa_test"
        }
    )
    assert response.status_code == 400