from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.text import Truncator


class User(AbstractUser):
    """Custom user model"""
    GENDER_CHOICES = {
        ('M', 'Male'),
        ('F', 'Female'),
    }

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    friends = models.ManyToManyField('self', blank=True)

    def get_avatar_url(self):
        if self.avatar:
            return self.avatar.url
        return ''


class Post(models.Model):
    text = models.TextField()
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    date_posted = models.DateTimeField(auto_now_add=True)  # Date and time set at object creation
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        truncated_text = Truncator(self.text)
        return truncated_text.chars(50)


class Comment(models.Model):
    text = models.TextField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    to = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    date_commented = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

    def __str__(self):
        truncated_text = Truncator(self.text)
        return truncated_text.chars(50)


class Message(models.Model):
    body = models.CharField(max_length=1000)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='messages_sent')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='messages_received')
    date_delivered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        truncated_body = Truncator(self.body)
        return truncated_body.chars(50)
