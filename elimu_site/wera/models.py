from django.db import models
from django.contrib.auth.models  import User


# Create your models here.
#creating our tables inside here

class Topic(models.Model):
    name = models.CharField(max_length=200)
    

    def __str__(self):
        return self.name





class Room(models.Model):
    host = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    #relationship between imported User and  host Column in Room Table
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    #relationship between    class Topic  and column topic in room table. 
    name  = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, 
        related_name='participants',blank=True 
        )
    updated = models.DateTimeField(auto_now=True)
    created  = models.DateTimeField(auto_now_add=True)
    # has a many to many relationship where a  participant can have many rooms and many
    # room can have many participants
       
    class Meta:
        ordering = ['-updated','-created']

    def  __str__(self): 
        return self.name
    #converting an object of the class to a string that returns name
    #as the attribute
    
    

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)    
    body = models.TextField()
    updated  =  models.DateField(auto_now=True)
    created  =  models.DateField(auto_now_add=True)
    
    def __str(self):
        return self.body[0:50]
    
    class Meta:
        ordering  = ['-updated', '-created']