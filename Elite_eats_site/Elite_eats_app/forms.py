from django.forms import ModelForm
from .models import Post, Image, Restaurant

class PostForm(ModelForm):
    class Meta:
        model = Post
        restaurant = Restaurant.objects.all()
        fields = ['restaurant', 'review']

class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'image',)

class UpdateForm(ModelForm):
    class Meta:
        model = Post
        restaurant = Restaurant.name
        fields = ['review', 'restaurant']

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'image')
