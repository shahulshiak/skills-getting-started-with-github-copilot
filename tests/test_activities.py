from src.app import activities


def test_get_activities_returns_all_activities(client):
    # Arrange
    expected_names = set(activities.keys())

    # Act
    response = client.get("/activities")
    response_data = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(response_data, dict)
    assert set(response_data.keys()) == expected_names


def test_get_activities_returns_required_fields_for_each_activity(client):
    # Arrange
    required_fields = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")
    response_data = response.json()

    # Assert
    assert response.status_code == 200
    for activity in response_data.values():
        assert set(activity.keys()) == required_fields


def test_get_activities_returns_participants_as_lists(client):
    # Arrange
    participants_key = "participants"

    # Act
    response = client.get("/activities")
    response_data = response.json()

    # Assert
    assert response.status_code == 200
    for activity in response_data.values():
        assert isinstance(activity[participants_key], list)
        assert all(isinstance(email, str) for email in activity[participants_key])
