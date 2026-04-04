from app.security import decode_access_token


def test_system_flow(client):
    user_payload = {
        "name": "Ana Souza",
        "email": "ana@email.com",
        "password": "12345678",
    }
    create_user = client.post("/users/", json=user_payload)
    assert create_user.status_code == 201
    user_id = create_user.json()["user_id"]

    task_payload = {
        "title": "Montar portfólio",
        "description": "Subir API no GitHub",
        "user_id": user_id,
    }
    create_task = client.post("/tasks/", json=task_payload)
    assert create_task.status_code == 201
    task_id = create_task.json()["task_id"]

    get_task = client.get(f"/tasks/{task_id}")
    assert get_task.status_code == 200
    assert get_task.json()["title"] == "Montar portfólio"

    patch_task = client.patch(f"/tasks/{task_id}", json={"completed": True})
    assert patch_task.status_code == 200
    assert patch_task.json()["completed"] is True

    list_tasks = client.get("/tasks/")
    assert list_tasks.status_code == 200
    assert len(list_tasks.json()) == 1


def test_login_returns_jwt_token(client):
    client.post(
        "/users/",
        json={
            "name": "Carlos",
            "email": "carlos@email.com",
            "password": "12345678",
        },
    )

    response = client.post(
        "/auth/login",
        json={
            "email": "carlos@email.com",
            "password": "12345678",
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["token_type"] == "bearer"
    assert isinstance(body["access_token"], str)

    payload = decode_access_token(body["access_token"])
    assert payload is not None
    assert "sub" in payload


def test_login_with_wrong_password_returns_401(client):
    client.post(
        "/users/",
        json={
            "name": "Bianca",
            "email": "bianca@email.com",
            "password": "12345678",
        },
    )

    response = client.post(
        "/auth/login",
        json={
            "email": "bianca@email.com",
            "password": "senha-errada",
        },
    )
    assert response.status_code == 401
