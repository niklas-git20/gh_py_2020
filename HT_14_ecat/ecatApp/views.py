from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import ProductForm
## relative import of forms 
from .models import ItemModel 
from .forms import ItemForm

# Create your views here.
def prod_view(request): 
    context ={} 
    context['form']= ItemForm() 
    return render(request, "home.html", context)

def create_view(request): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # add the dictionary during initialization 
    form = ItemForm(request.POST or None) 
    if form.is_valid(): 
        form.save() 
          
    context['form']= form 
    return render(request, "create_view.html", context)


def list_view(request): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # add the dictionary during initialization 
    context["dataset"] = ItemModel.objects.all() 
          
    return render(request, "list_view.html", context)


# pass id attribute from urls 
def detail_view(request, id): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # add the dictionary during initialization 
    context["data"] = ItemModel.objects.get(id = id) 
          
    return render(request, "detail_view.html", context) 

# update view for details 
def update_view(request, id): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # fetch the object related to passed id 
    obj = get_object_or_404(ItemModel, id = id) 
  
    # pass the object as instance in form 
    form = ItemForm(request.POST or None, instance = obj) 
  
    # save the data from the form and 
    # redirect to detail_view 
    if form.is_valid(): 
        form.save() 
        return HttpResponseRedirect("/"+id) 
  
    # add form dictionary to context 
    context["form"] = form 
  
    return render(request, "update_view.html", context) 


# delete view for details 
def delete_view(request, id): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # fetch the object related to passed id 
    obj = get_object_or_404(ItemModel, id = id)   
  
    if request.method =="POST": 
        # delete object 
        obj.delete() 
        # after deleting redirect to  
        # home page 
        return HttpResponseRedirect("/") 
  
    return render(request, "delete_view.html", context) 