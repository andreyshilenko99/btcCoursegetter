import os
from celery import Celery
from dotenv import load_dotenv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'btcCoursegetter.settings')
celery_app = Celery('btcCoursegetter')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()
load_dotenv()


@celery_app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
