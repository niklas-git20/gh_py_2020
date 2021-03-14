from __future__ import absolute_import
import os
from celery import Celery


# celery settings
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_scrape.settings')

app = Celery('django_scrape', 
		backend='rpc://', 
		broker='pyamqp://',
		include=['django_scrape.tasks'])
	
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

task_routes = {
    'tasks.scrape_task': 'low-priority',
}


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))