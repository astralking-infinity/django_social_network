from django import forms

from .models import Post, User


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['text', 'photo']


class AvatarForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['avatar']
