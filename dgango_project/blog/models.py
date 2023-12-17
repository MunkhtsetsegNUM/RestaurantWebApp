from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    comment = models.CharField(max_length=300)
    rate = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.comment
    
class Users(models.Model):
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=50)
    
class Person(models.Model):
    first_name = models.CharField(max_length=30)