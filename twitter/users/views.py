from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello there! You've reached the index page of the users app")

def users(request):
    return HttpResponse("Hello there! You've reached the users page of the users app")

def followers_following(request):
    return HttpResponse("Hello there! You've reached the followers_following page of the users app")

def tweets(request):
    return HttpResponse("Hello there! You've reached the tweets page of the users app")
