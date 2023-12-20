from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    comment = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.CharField(max_length = 30)
    rate = models.IntegerField()
    
    def __str__(self):
        return self.comment
    
class Users(models.Model):
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=50)
    
class Person(models.Model):
    first_name = models.CharField(max_length=30)
class Places(models.Model):
    pName = models.CharField(max_length = 100)
    types = models.CharField(max_length = 20)
    pImage = models.ImageField()
    rate = models.IntegerField()
    def __str__(self):
        return self.pName
    
    def get_avg_rating(self):
        reviews = Review.objects.filter(places=self)
        if reviews.exists():
            return sum(review.rate for review in reviews) / reviews.count()
        return 0
    
class Menu(models.Model):
    place = models.ForeignKey(Places, on_delete=models.CASCADE, related_name='menus')
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    fImage = models.ImageField(upload_to='')
    def __str__(self):
        return self.name