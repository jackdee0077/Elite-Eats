from django.contrib import admin
from .models import Post
from .models import Restaurant
from .models import Image
admin.site.register(Image)

from .models import Image
admin.site.register(Image)


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'state', 'zip_code',)

admin.site.register(Restaurant, RestaurantAdmin)


# Register your models here.
