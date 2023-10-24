from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, "layout.html")

def login_view(request):
    return render(request, "login.html")

def logout(request):
    return render(request, "logout.html")

def register(request):
    return render(request, "register.html")
