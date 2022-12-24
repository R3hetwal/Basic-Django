from django.db import models



class Todo(models.Model): # PascalCasing 
    title = models.CharField(max_length=200)
    

    # double underscore is known as dunder method
    def __str__(self): 
        return self.title # To view names of objects in admin panel