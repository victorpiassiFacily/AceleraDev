from fastapi.testclient import TestClient


def test_coupon_create(client: TestClient):
    response = client.post("/coupon/", json={
        "code": "ABC",
        "limit": 5,
        "type": "percentage",
        "value": 20
    })

    assert response.status_code == 201
    assert response.json()["id"] == 1


def test_coupon_index(client: TestClient):
    response = client.post("/coupon/", json={
        "code": "ABC",
        "limit": 5,
        "type": "percentage",
        "value": 20
    })

    assert response.status_code == 201

    response = client.get("/coupon/1")

    assert response.status_code == 200

    response = response.json()
    assert response["code"] == "ABC"
    assert response["limit"] == 5
    assert response["type"] == "percentage"
    assert response["value"] == 20


def test_coupon_update(client: TestClient):
    response = client.post("/coupon/", json={
        "code": "ABC",
        "limit": 5,
        "type": "percentage",
        "value": 20
    })

    assert response.status_code == 201

    response = client.put("/coupon/1", json={
        "code": "ABC",
        "limit": 4,
        "type": "value",
        "value": 200
    })

    assert response.status_code == 200

    response = response.json()
    assert response["code"] == "ABC"
    assert response["limit"] == 4
    assert response["type"] == "value"
    assert response["value"] == 200


def test_coupon_show(client: TestClient):
    response = client.post("/coupon/", json={
        "code": "ABC",
        "limit": 5,
        "type": "percentage",
        "value": 20
    })
    assert response.status_code == 201

    response = client.post("/coupon/", json={
        "code": "BCD",
        "limit": 10,
        "type": "percentage",
        "value": 25
    })
    assert response.status_code == 201

    response = client.get("/coupon")

    assert response.status_code == 200

    response = response.json()

    assert len(response) == 2
    assert response[0]["code"] == "ABC"
    assert response[0]["limit"] == 5
    assert response[0]["type"] == "percentage"
    assert response[0]["value"] == 20

    assert response[0]["code"] == "BCD"
    assert response[0]["limit"] == 10
    assert response[0]["type"] == "percentage"
    assert response[0]["value"] == 25

    assert response[0]["code"] != response[1]["code"]


def test_coupon_remove(client: TestClient):
    response = client.post("/coupon/", json={
        "code": "ABC",
        "limit": 5,
        "type": "percentage",
        "value": 20
    })
    assert response.status_code == 201

    response = client.delete("/coupon/1")

    assert response.status_code == 200
    assert response.json() == {}
