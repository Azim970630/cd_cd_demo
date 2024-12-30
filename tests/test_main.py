from app.main import create_app


def test_health_check():
    """Test the health check endpoint"""
    app = create_app()
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}


def test_version():
    """Test the version endpoint"""
    app = create_app()
    client = app.test_client()
    response = client.get("/api/v1/version")
    assert response.status_code == 200
    assert response.json == {"version": "1.0"}
