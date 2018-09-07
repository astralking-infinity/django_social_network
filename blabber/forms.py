from django import forms

from .models import Comment, Post, User


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['text', 'photo']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4})
        }


class AvatarForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['avatar']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 2})
        }
