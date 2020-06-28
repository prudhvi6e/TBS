from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('artist', views.artist, name="artist"),
    path('blog', views.blog, name="blog"),
    path('category', views.category, name="category"),
    path('contact', views.contact, name="contact"),
    path('playlist', views.playlist, name="playlist"),
]