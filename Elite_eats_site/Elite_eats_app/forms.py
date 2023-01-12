from django.forms import ModelForm
from Elite_eats_app.models import Post, Image
from django import forms

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['review']

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'image')