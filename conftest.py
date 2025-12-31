# import pytest
# from src.clients import Petclient

# @pytest.fixture(scope="session")
# def pet_client_fixture():
#     client_obj = Petclient()
#     return client_obj

import pytest
from src.clients.pet_client import Petclient

@pytest.fixture(scope="session")
def pet_client_fixture():
    return Petclient()
