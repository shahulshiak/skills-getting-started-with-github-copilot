from copy import deepcopy
from urllib.parse import quote

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app

_INITIAL_ACTIVITIES = deepcopy(activities)


def activity_path(activity_name: str) -> str:
    return quote(activity_name, safe="")


@pytest.fixture(autouse=True)
def reset_activities() -> None:
    activities.clear()
    activities.update(deepcopy(_INITIAL_ACTIVITIES))
    yield
    activities.clear()
    activities.update(deepcopy(_INITIAL_ACTIVITIES))


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)
