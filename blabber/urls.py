from django.urls import path

from . import views

app_name = 'blabber'

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('<slug:username>/', views.ProfileView.as_view(), name='profile'),
]
