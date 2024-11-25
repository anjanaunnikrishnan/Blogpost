import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_generate_endpoint(client):
    response = client.post('/generate', json={'prompt': 'Hello World!'})
    assert response.status_code == 200
    assert 'generated_content' in response.json
    assert response.json['generated_content'] == "Processed prompt: Hello World!"

def test_generate_missing_prompt(client):
    response = client.post('/generate', json={})
    assert response.status_code == 400
    assert response.json['error'] == 'Prompt is required'
