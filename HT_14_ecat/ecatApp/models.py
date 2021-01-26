from django.db import models

# Create your models here.
# declare a new model 
class ItemModel(models.Model): 
  
    # fields of the model
    ident = models. IntegerField()
    title = models.CharField(max_length = 20) 
    description = models.TextField() 
  
    # renames the instances of the model 
    # with their title name 
    def __str__(self): 
        return self.ident, self.title, self.description

# after creation in command line run commands to create Database
# Python manage.py makemigrations
# Python manage.py migrate