import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_gems.settings')

app = Celery('django_gems')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    'cleanup_expired_carts_task': {
        'task': 'django_gems.shopping-cart.tasks.cleanup_expired_carts',
        'schedule': 3600,
    },
}
