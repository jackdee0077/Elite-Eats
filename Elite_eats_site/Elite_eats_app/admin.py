from django.contrib import admin

from .models import Restaurant

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'state', 'zip_code',)

admin.site.register(Restaurant, RestaurantAdmin)

# Register your models here.
