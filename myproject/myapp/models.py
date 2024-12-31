from django.db import models

# Create your models here.OOP.ORM
class Tour(models.Model):
    # origin country,destination,number of nights, price for tour
    origin_country = models.CharField(max_length=64)
    destination_country = models.CharField(max_length=64) 
    number_of_nights = models.IntegerField()
    price = models.IntegerField()
    
    # this is a string representation of the tours
    def __str__(self):
        return(f"ID:{self.id}: From {self.origin_country} To {self.destination_country}, {self.number_of_nights} nights costs ${self.price}")
        
        
        
        
        
# models.py
# create a model in order to make the table for the form model

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.name} ({self.email})"
