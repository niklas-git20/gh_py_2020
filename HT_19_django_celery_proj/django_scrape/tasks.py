from __future__ import absolute_import
import string
from crontab import CronTab

from celery import Celery
from .celery import app


# celery tasks
from celery import shared_task
# periodic tasks

from celery.decorators import periodic_task, task

from scripts.scrape import scrape
# from django_scrape.views import results


# go to project folder: C:\Users\Nik\Desktop\gh_py_temp\django_celery_proj\django_scrape
# run worker: celery -A django_scrape worker --loglevel=INFO

# shared_task: no concrete function is required
# run task file: python -m django_scrape.tasks
# or use python console
# $ python ./manage.py shell
# >>> from django_scrape.tasks import sum
# >>> res = sum.delay(2,3)
# >>> res.state # PENDING
# >>> res.get()
# >>> res.state # SUCCESS

# check task route in worker

# use extension
# install django_celery_results
# modify settings.py 
# INSTALLED_APPS = (
#   ...,
#    'django_celery_results',)
# migrate database
# $ python manage.py migrate

# django-celery-beat - Database-backed Periodic Tasks with Admin interface
# install django-celery-beat
# modify settings.py 
# INSTALLED_APPS = (
#   ...,
#    'django_celery_results',)
# migrate database
# $ python manage.py migrate
# start the celery beat service django_celery_beat.schedulers:DatabaseScheduler scheduler:
# celery -A django_scrape beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
# in Django-Admin set periodic tasks.





@shared_task()
def sum(a,b):
	return a + b

@app.task()
def scrape_task(url, quant):
	r = []
	r = scrape(url, quant)
	return r


# @periodic_task(
#     run_every=(crontab(minute='1')),
#     name="view_render",
#     ignore_result=True)
# def view_render():
# 	scrape_result = results(url, quant)
# 	return scrape_result

if __name__ == '__main__':
	# url1 = 'https://www.olx.ua/elektronika/kompyutery-i-komplektuyuschie/nastolnye-kompyutery/'
	# quant1 = 2
	# advert_data = scrape_task(url1, quant1)
	# print(r1)

	s1 = sum(2,2)
	print(s1)




	
