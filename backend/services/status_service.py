def get_status_data():
    return {
        "status": "ok",
        "message": "Backend работает успешно",
        "service": "APIFlask Backend",
        "items_count": 3
    }

def get_items_data():
    return [
        {"id": 1, "name": "Первый элемент"},
        {"id": 2, "name": "Второй элемент"},
        {"id": 3, "name": "Третий элемент"}
    ]
