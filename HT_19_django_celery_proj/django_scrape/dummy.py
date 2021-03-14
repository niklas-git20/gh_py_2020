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
    cache_data = cache.get('data')
#   if task_state == 'SUCCESS':    
    advert_data = scrape(url, quant) 
    return render(request, 'results2.html/', 
            {'task_state': task_state,
    #        'advert_data': advert_data,
            'cache_data': cache_data,
                })