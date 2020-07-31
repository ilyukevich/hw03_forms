from django import forms
from .models import Post
from django.forms import ModelForm
#from django.core.exceptions import ValidationError

#revision

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['group', 'text']

form = PostForm()
