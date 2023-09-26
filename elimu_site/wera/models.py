from django.db import models

# Create your models here.
#creating our tables inside here

class Room(models.Model):
    #host = 
    #topic=
    name  = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    #participants
    updated = models.DateField(auto_now=True)
    created  = models.DateField(auto_now_add=True)


    def  __str__(self):
        return self.name
    #converting an object of the class to a string that returns name
    #as the attribute