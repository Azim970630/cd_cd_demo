import pytest

from app import create_app


@pytest.fixture
def client():
    """Create test client"""
    app = create_app()
    return app.test_client()


@pytest.mark.integration
def test_health_endpoint(client):
    """Test health endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}


@pytest.mark.integration
def test_version_endpoint(client):
    """Test version endpoint"""
    response = client.get("/api/v1/version")
    assert response.status_code == 200
    assert response.json == {"version": "1.0"}
