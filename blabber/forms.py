from django import forms

from .models import Post, User


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
