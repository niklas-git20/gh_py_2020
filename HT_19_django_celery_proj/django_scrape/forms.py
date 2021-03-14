from django import forms 
from .models import AdvertModel
  

# creating a form 
class AdvertForm(forms.ModelForm): 

    # create meta class 
    class Meta: 
        # specify model to be used         
        model = AdvertModel
  
        # specify fields to be used 
        fields = [ 
        	"ident",
            "url",
            "title", 
            "seller",
            "description", 
            "phone"
			] 
    