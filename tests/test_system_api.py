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
