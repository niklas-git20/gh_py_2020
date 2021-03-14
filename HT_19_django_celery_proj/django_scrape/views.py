from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
import subprocess
from scripts.scrape import scrape

# celery tasks
from celery import shared_task
from .celery import app
from .tasks import scrape_task



def search(request):
    return render(request, 'search.html')
    

def results(request):
    # take values from search form
    url = request.GET['advert_url']
    quant = request.GET['advert_quant'] 
    
    # call script function      
    advert_data = scrape_task.delay(url, quant) 
    # advert_data = scrape_task.apply_async((url, quant), queue='scrape', countdown=10)
    advert_data.get() 
    task_state = advert_data.state
    advert_data.get() 
#   if task_state == 'SUCCESS':    
    advert_data = scrape(url, quant) 
    return render(request, 'results2.html/', 
                {'task_state': task_state,
                'advert_data': advert_data,
                    })
#    return HttpResponse(task_state, 'scrapping')

## chain
# need to test
# def results(request):
#     # take values from search form
#     url = request.GET['advert_url']
#     quant = request.GET['advert_quant'] 
#     return HttpResponse('scrapping url')    


# def task_run(request, url): 
#     # call script func
#     task = scrape_task.delay(url, quant)
#     context['task_id'] = task.id
#     context['task_status'] = task.status
#     return render (request, 'results3.html')

# def task_view(request, task_id):   
#     task = app.AsyncResult(task_id)       
#     advert_data =  {'task_status': task.status, 'task_id': task.id}
#     if task.status == 'SUCCESS':
#             advert_data['results'] = task.get()
#     return JsonResponse(advert_data)


 
        




# def script_func(url, quant):
#     print(url, quant)
#     subprocess.run(['python', 'scripts//scrape.py', url, str(quant)], 
#         shell=False, timeout=1800)
