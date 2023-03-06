
from django.forms import ModelForm
from .models import Comment, Image, Restaurant
from .models import Comment, Image, Restaurant
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Comment
        restaurant = Restaurant.objects.all()
        fields = ['restaurant', 'review']

class UpdateForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['review']
        restaurant = Restaurant.name
        fields = ['review', 'restaurant']

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'image')
