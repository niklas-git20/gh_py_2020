from django.db import models

# Create your models here.
# declare a new model 
class AdvertModel(models.Model):   
    # fields of the model
    ident = models. IntegerField()
    url = models.TextField()
    title = models.CharField(max_length = 20) 
    seller = models.CharField(max_length = 20)
    description = models.TextField()
    phone = models.IntegerField() 
  
    # renames the instances of the model 
    # with their title name 
    def __str__(self): 
        return self.ident, self, url, self.title, self.seller, 
        	self.description, self.phone 


# after creation in command line run commands to create Database
# Python manage.py makemigrations
# Python manage.py migrate