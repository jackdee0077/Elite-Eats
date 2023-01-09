from django.forms import ModelForm
from Elite_eats_app.models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['review']