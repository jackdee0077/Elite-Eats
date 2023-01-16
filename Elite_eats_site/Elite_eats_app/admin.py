from django.contrib import admin
from .models import Post
from .models import Restaurant
from .models import Image
admin.site.register(Image)


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'state', 'zip_code')

class PostAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'review')

class TagAdmin(admin.ModelAdmin):
    list_display = ('restaraunt' , 'hashtag')


# Register your models here.
admin.site.register(Restaurant, RestaurantAdmin)






# Register your models here.
