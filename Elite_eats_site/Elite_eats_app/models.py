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

