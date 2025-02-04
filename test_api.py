import requests
import pytest

BASE_URL = "https://reqres.in/api"

def test_get_user():
    """ Test GET request to fetch user details """
    response = requests.get(f"{BASE_URL}/users/2")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    json_data = response.json()
    assert json_data["data"]["id"] == 2, "User ID mismatch"
    assert "email" in json_data["data"], "Email not found in response"
    assert "first_name" in json_data["data"], "First name not found"
    assert "last_name" in json_data["data"], "Last name not found"

def test_create_user():
    """ Test POST request to create a new user """
    payload = {"name": "morpheus", "job": "leader"}
    response = requests.post(f"{BASE_URL}/users", json=payload)
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"
    json_data = response.json()
    assert json_data["name"] == "morpheus", "Name mismatch"
    assert json_data["job"] == "leader", "Job mismatch"
    assert "id" in json_data, "ID not found in response"
    assert "createdAt" in json_data, "createdAt field missing"

if __name__ == "__main__":
    pytest.main(["-v"])

