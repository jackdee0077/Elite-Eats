from django.db import models


# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=60)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)

    zip_code = models.CharField(max_length=5);

    class Meta:
        verbose_name_plural = "Elite_eats_app"
    
    def _str_(self):
        return self.name

    zip_code = models.CharField(max_length=5)

class Post(models.Model):
    review = models.CharField(max_length=1500)

   #we made this image( was post )
class Image(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)