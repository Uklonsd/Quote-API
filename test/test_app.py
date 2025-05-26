import pytest
from app.app import app
from app.models import Quote
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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
  data = response.get_json()
  engine = create_engine('sqlite:///quotes.db')
  Session = sessionmaker(bind=engine)
  session = Session()

  quote = session.get(Quote, data['id'])
  assert quote is not None
  assert quote.quote == data['quote']
  assert quote.image == data['image']
