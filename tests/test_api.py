from fastapi.testclient import TestClient

from src.app import app, activities

client = TestClient(app)


def test_unregister_participant_removes_email():
    activity_name = "Chess Club"
    email = "michael@mergington.edu"

    response = client.delete(f"/activities/{activity_name}/participants?email={email}")

    assert response.status_code == 200
    assert email not in activities[activity_name]["participants"]
    assert response.json()["message"] == f"Unregistered {email} from {activity_name}"

    activities[activity_name]["participants"].append(email)


def test_unregister_missing_participant_returns_404():
    activity_name = "Chess Club"
    email = "missing-student@mergington.edu"

    response = client.delete(f"/activities/{activity_name}/participants?email={email}")

    assert response.status_code == 404
