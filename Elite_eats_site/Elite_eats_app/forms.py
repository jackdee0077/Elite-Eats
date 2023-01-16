
from django.forms import ModelForm
from .models import Post, Image, Restaurant, Tag

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        restaurant = Restaurant.objects.all()
        hastag = Tag.hashtag
        fields = ['restaurant', 'review', 'hashtag' ]

class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'image',)

class UpdateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['review']
        restaurant = Restaurant.name
        fields = ['review', 'restaurant']

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'image')
