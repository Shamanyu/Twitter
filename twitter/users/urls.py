from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.index, name='users'),
    path('followers_following/', views.index, name='followers_following'),
    path('tweets/', views.index, name='tweets'),
]
