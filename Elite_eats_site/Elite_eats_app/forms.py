from django.forms import ModelForm
from .models import Post, Image, Restaurant

class PostForm(ModelForm):
    class Meta:
        model = Post
        restaurant = Restaurant.name
        fields = ['review', 'restaurant']

class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'image',)