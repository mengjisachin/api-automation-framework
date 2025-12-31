import pytest
from src.data.pet_data import create_pet_payload

@pytest.mark.parametrize(
    "pet_id, name, status",
    [
        (101, "dog", "available"),
        (102, "cat", "sold"),
        (103, "rabbit", "pending"),
    ]
)
def test_create_pet_param(pet_client_fixture, pet_id, name, status):
    payload = create_pet_payload(pet_id, name, status)
    response = pet_client_fixture.add_petbyID(payload)

    assert response.status_code == 200
    assert response.json()["id"] == pet_id


        

        