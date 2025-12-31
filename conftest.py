import pytest
from src.clients.pet_client import Petclient

@pytest.fixture(scope="session")
def pet_client_fixture():
    return Petclient()
