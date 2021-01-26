from django import forms 
from .models import ItemModel
  
# creating a form  
class ProductForm(forms.Form):       
    prod_number = forms.IntegerField() 
    prod_name = forms.CharField(max_length = 200) 
    prod_descr = forms.CharField(max_length = 200) 
    # methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])


# creating a form 
class ItemForm(forms.ModelForm): 

    # create meta class 
    class Meta: 
        # specify model to be used         
        model = ItemModel
  
        # specify fields to be used 
        fields = [ 
        	"ident",
            "title", 
            "description", 
			] 
    