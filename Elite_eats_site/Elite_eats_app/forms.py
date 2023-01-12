from .models import Post, Image, Restaurant
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        restaurant = Restaurant.name
        fields = ['review', 'restaurant']

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'image')
