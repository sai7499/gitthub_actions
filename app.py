from app import app

def test_homepage():
    tester = app.test_client()
    # print("Testing homepage...")
    response = tester.get("/")
    assert response.status_code == 200
