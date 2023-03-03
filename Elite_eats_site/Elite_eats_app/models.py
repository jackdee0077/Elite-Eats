from django.db import models
# from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.urls import reverse


# Create your models here.
class Tag(models.Model):
    hashtag = models.CharField(max_length=100)

    def __str__(self):
        return self.hashtag
        

class Restaurant(models.Model):
    name = models.CharField(max_length=80)
    address = models.CharField(max_length=60)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5)
    hashtag = models.ManyToManyField(Tag, blank=True)
    
    class Meta:
        verbose_name_plural = "Restaurants"
    
    def __str__(self):
        return self.name

class Post(models.Model):
    restaurant = models.ForeignKey(Restaurant, blank=True, null=True, on_delete=models.CASCADE)
    review = models.TextField(max_length=1500)
    hashtag = models.ManyToManyField(Tag, blank=True)


'''
   #we made this image( was post )
class Image(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    # zip_code = models.CharField(max_length=5)

    #This looks like a duplicate (Tony and VAl)
'''

class Post(models.Model):
    restaurant = models.ForeignKey(Restaurant, blank=True, null=True, on_delete=models.CASCADE)
    review = models.TextField(max_length=1500)


   #we made this image( was post )
class Image(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.image
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
