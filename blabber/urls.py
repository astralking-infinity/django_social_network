from django.urls import path

from . import views

app_name = 'blabber'

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('<slug:username>/', views.ProfileView.as_view(), name='profile'),
    path('avatar/change/<int:pk>/', views.AvatarView.as_view(), name='avatar'),
    path('posts/<int:pk>/like/', views.LikeToggleView.as_view(), name='like_toggle'),
    path('posts/add_post/', views.PostFormView.as_view(), name='add_post'),
    path('posts/<int:pk>/comment/', views.CommentFormView.as_view(), name='comment'),
]
