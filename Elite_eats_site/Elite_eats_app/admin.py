from django.contrib import admin
from .models import Comment , Restaurant , Image, SiteUsers


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'state', 'zip_code')

class PostAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'review')

class TagAdmin(admin.ModelAdmin):
    list_display = ('restaraunt' , 'hashtag')


# Register your models here.
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Comment, PostAdmin)
admin.site.register(Image)
admin.site.register(SiteUsers)








# Register your models here.
