from fastapi.testclient import TestClient
import json
import pandas as pd
import pytest

from server import app

TEST_PATH = "data.csv"

FEATURES = [
  "age",
  "sex",
  "cp",
  "trestbps",
  "chol",
  "fbs",
  "restecg",
  "thalach",
  "exang",
  "oldpeak",
  "slope",
  "ca",
  "thal",
]

client = TestClient(app)

def test_health_check():
    response = client.get("/health_check")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_predict_valid(test_data):
    x = test_data[FEATURES]

    response = client.post("/predict", json=x.to_json())
    assert response.status_code == 200

    data = json.loads(response.json())
    assert data  == [1, 1, 0, 0]

@pytest.fixture
def test_data():
    return pd.read_csv(TEST_PATH)
