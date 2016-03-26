from django import forms
from django.forms import modelform_factory
from .models import Post

# class PostForm(forms.ModelForm):

# 	class Meta:
# 		model = Post
# 		fields = ('title', 'content',)

PostForm = modelform_factory(Post, fields=('title', 'content'))