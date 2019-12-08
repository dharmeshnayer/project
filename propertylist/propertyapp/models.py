from django.db import models
from django.contrib.auth.models import User


class Property(models.Model):
    name =  models.CharField(max_length=400)
    description = models.TextField()
    price = models.FloatField()
    author = models.ForeignKey(User)
    
    

    
    

# Create your models here.
