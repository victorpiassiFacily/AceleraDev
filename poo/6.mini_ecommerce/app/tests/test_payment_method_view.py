from fastapi.testclient import TestClient


def test_payment_method_create(client: TestClient):
    response = client.post("/payment-method/", json={
        "product_id": 1,
        "mode": "value",
        "value": 150,
        "payment_method_id": 1
    })

    assert response.status_code == 201
    assert response.json()["id"] == 1


def test_payment_method_index(client: TestClient):
    response = client.post("/payment-method/", json={
        "product_id": 1,
        "mode": "value",
        "value": 150,
        "payment_method_id": 1
    })

    assert response.status_code == 201

    response = client.get("/payment-method/1")

    assert response.status_code == 200

    response = response.json()
    assert response["product_id"] == 1  # product.id
    assert response["mode"] == "value"
    assert response["value"] == 150
    assert response["payment_method_id"] == 1  # payment_method.id


def test_payment_method_update(client: TestClient):
    response = client.post("/payment-method/", json={
        "product_id": 1,
        "mode": "value",
        "value": 150,
        "payment_method_id": 1
    })

    assert response.status_code == 201

    response = client.put("/payment-method/1", json={
        "product_id": 1,
        "mode": "percentage",
        "value": 15,
        "payment_method_id": 1
    })

    assert response.status_code == 200

    response = response.json()
    assert response["product_id"] == 1  # product.id
    assert response["mode"] == "percentage"
    assert response["value"] == "15"
    assert response["payment_method_id"] == 1  # payment_method.id


def test_payment_method_show(client: TestClient):
    response = client.post("/payment-method/", json={
        "product_id": 1,
        "mode": "value",
        "value": 150,
        "payment_method_id": 1
    })
    assert response.status_code == 201

    response = client.post("/payment-method/", json={
        "product_id": 1,
        "mode": "percentage",
        "value": 15,
        "payment_method_id": 2
    })
    assert response.status_code == 201

    response = client.get("/payment-method")

    assert response.status_code == 200

    response = response.json()

    assert len(response) == 2
    assert response[0]["product_id"] == 1
    assert response[0]["mode"] == "value"
    assert response[0]["value"] == 150
    assert response[0]["payment_method_id"] == 1

    assert response[0]["product_id"] == 1
    assert response[0]["mode"] == "percentage"
    assert response[0]["value"] == 15
    assert response[0]["payment_method_id"] == 2
