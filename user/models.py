from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, IntegerField

class Events(models.Model):
    title = CharField(max_length=100)
    year = IntegerField()
    image = CharField(max_length=800)
    description = CharField(max_length=500) 
    date =CharField(max_length=100) 
    capacity = CharField(max_length=100) 
    price =CharField(max_length=100) 

class Cart(models.Model):
    movie = models.ForeignKey(Events, on_delete=CASCADE)
    user = models.ForeignKey(User, on_delete=CASCADE)
    number = IntegerField(default=1)



class Ticket(models.Model):
    movie = models.ForeignKey(Events, on_delete=CASCADE)
    user = models.ForeignKey(User, on_delete=CASCADE)
    code = CharField(max_length=16)

