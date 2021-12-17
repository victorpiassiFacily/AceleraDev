from fastapi.testclient import TestClient


def test_supplier_create(client: TestClient):
    response = client.post("/supplier/", json={
        "name": "Fornecedor 1"
    })

    assert response.status_code == 201
    assert response.json()["id"] == 1


def test_supplier_index(client: TestClient):
    response = client.post("/supplier/", json={
        "name": "Fornecedor 1"
    })

    assert response.status_code == 201

    response = client.get("/supplier/1")

    assert response.status_code == 200
    assert response.json()["name"] == "Fornecedor 1"


def test_supplier_update(client: TestClient):
    response = client.post("/supplier/", json={
        "name": "Fornecedor 1"
    })

    assert response.status_code == 201

    response = client.put("/supplier/1", json={
        "name": "Categoria Alterada"
    })

    assert response.status_code == 200
    assert response.json()["name"] == "Categoria Alterada"


def test_supplier_show(client: TestClient):
    response = client.post("/supplier/", json={
        "name": "Fornecedor 1"
    })
    assert response.status_code == 201

    response = client.post("/supplier/", json={
        "name": "Fornecedor 2"
    })
    assert response.status_code == 201

    response = client.get("/supplier")

    assert response.status_code == 200

    response = response.json()

    assert len(response) == 2
    assert response[0]["name"] == "Fornecedor 1"
    assert response[1]["name"] == "Fornecedor 2"
