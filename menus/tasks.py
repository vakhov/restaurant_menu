from restaurant_menu.celery import app


@app.task
def hello():
    """Тестовая таск задача"""
    print("Hello World!")
