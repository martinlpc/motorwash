from django.shortcuts import render
from .models import *


# Create your views here.
def home(request):
    return render(request, "myapp/index.html")


def employees(request):
    context = {"employees": Employee.objects.all()}
    return render(request, "myapp/employees.html", context)


def vehicles(request):
    context = {"vehicles": Vehicle.objects.all()}
    return render(request, "myapp/vehicles.html", context)


def clients(request):
    context = {"Clients": Client.objects.all()}
    return render(request, "myapp/clients.html", context)


def tasks(request):
    context = {"tasks": Task.objects.all()}
    return render(request, "myapp/tasks.html", context)
