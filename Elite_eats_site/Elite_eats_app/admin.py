from django.contrib import admin

from .models import Restaurant, Image, Post, Tag



class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'state', 'zip_code')

class PostAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'review')

class TagAdmin(admin.ModelAdmin):
    list_display = ('hashtag',)

class ImageAdmin(admin.ModelAdmin):
    list_display = ('title' , 'image')


# Register your models here.
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
# Register your models here.
