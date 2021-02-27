from django.http import HttpResponse
from django.shortcuts import render
import subprocess


def search(request):
    return render(request, 'search.html')
    

def results(request):
    # take values from search form
    url = request.GET['advert_url']
    quant = request.GET['advert_quant']

    # call script function
    from scripts.scrape import scrape
    # data = script_func(url, quant)  
    
    advert_data = scrape(url, quant)
    
    
    return render(request, 'results.html', 
        {'advert_data': advert_data
            })


# def script_func(url, quant):
#     print(url, quant)
#     subprocess.run(['python', 'scripts//scrape.py', url, str(quant)], 
#         shell=False, timeout=1800)
