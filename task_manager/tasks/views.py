from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, "tasks/index.html")

def details(request):
    return render(request, "tasks/details.html")

def signin(request):
    return render(request, "tasks/signin.html")