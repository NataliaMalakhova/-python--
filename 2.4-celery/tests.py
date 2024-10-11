import pytest
from io import BytesIO
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_upscale(client):
    data = {'file': (BytesIO(b'my file contents'), 'test.png')}
    response = client.post('/upscale', content_type='multipart/form-data', data=data)
    assert response.status_code == 202
    assert 'task_id' in response.json
