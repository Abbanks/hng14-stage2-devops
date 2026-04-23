import pytest
from fastapi.testclient import TestClient
from fakeredis import FakeRedis
from main import app, r 

client = TestClient(app)

@pytest.fixture(autouse=True)
def mock_redis(monkeypatch):
    """
    Overwrites the redis instance in main.py with a FakeRedis instance
    for the duration of the tests.
    """
    fake_r = FakeRedis()
    monkeypatch.setattr("main.r", fake_r)
    return fake_r

def test_create_job():
    """Test 1: Assert job creation returns a valid UUID and status code 201/200"""
    response = client.post("/jobs")
    assert response.status_code == 200
    assert "job_id" in response.json()

def test_get_job_status_queued():
    """Test 2: Assert that a newly created job defaults to 'queued'"""
    create_res = client.post("/jobs")
    job_id = create_res.json()["job_id"]
    
    response = client.get(f"/jobs/{job_id}")
    assert response.status_code == 200
    assert response.json()["status"] == "queued"

def test_get_nonexistent_job():
    """Test 3: Assert that a fake job ID returns a 404 error"""
    response = client.get("/jobs/this-id-does-not-exist")
    assert response.status_code == 404
    assert response.json()["detail"] == "Job not found"