import pytest
from app.app import app, QUETOS

@pytest.fixture
def client():
  app.testing = True
  with app.test_client() as client:
    yield client

def test_quote_status_code(client):
  response = client.get('/quote')
  assert response.status_code == 200

def test_quote_structure(client):
  response = client.get('/quote')
  data = response.get_json()
  assert 'author' in data
  assert 'quote' in data
  assert 'image' in data
  assert isinstance(data['author'], str)
  assert isinstance(data['quote'], str)
  assert isinstance(data['image'], str) or data['image'] is None

def test_quote_validity(client):
  response = client.get('/quote')
  data = response.get_json
  author = data['author']
  assert author in QUOTES
  assert data['quote'] == QUOTES[author]['quote']
  if 'image' in QUOTES[author]:
    assert data['image'] == QUOTES[author]['image']

