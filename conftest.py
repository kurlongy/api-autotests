import pytest
import requests

@pytest.fixture
def session():
    session = requests.Session()
    yield session
    session.close()