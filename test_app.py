from flask import json
from app import app


def test_hello():
    client = app.test_client()
    response = client.get('/hello')
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, World!"}


def test_echo():
    client = app.test_client()
    payload = {"msg": "ping"}
    response = client.post('/echo', json=payload)
    assert response.status_code == 201
    assert json.loads(response.data) == payload


def test_echo_put():
    client = app.test_client()
    echo_id = 1
    payload = {
        "id": echo_id,
        "msg": "hello, this is a message I want to test"}
    response = client.put(f"/echo/{echo_id}", json=payload)
    assert response.status_code == 201
    assert json.loads(response.data) == payload


def test_echo_delete():
    client = app.test_client()
    echo_id = 1

    # Arrange: add an echo
    app.echos[echo_id] = {"id": echo_id, "msg": "test message"}

    response = client.delete(f"/echo/{echo_id}")
    assert response.status_code == 200
    assert json.loads(response.data) == {"message": "Echo has been deleted!"}
