""" настройки celery """

broker_url = 'redis://redis:6379'
result_backend = 'redis://redis:6379'
accept_content = ['application/json']
result_serializer = 'json'
task_serializer = 'json'

timezone = 'Asia/Yekaterinburg'
worker_max_tasks_per_child = 1

beat_schedule = {
    'hello': {
        'task': 'menus.tasks.pastebin',
        'schedule': 60 * 60 * 1
    }
}
