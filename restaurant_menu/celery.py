import os
from celery import Celery, Task

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant_menu.settings')

app = Celery('restaurant_menu')

app.config_from_object('restaurant_menu.celeryconfig', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
