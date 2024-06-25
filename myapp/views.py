from django.shortcuts import render
from .models import *


# Create your views here.
def home(request):
    return render(request, "index.html")


def employees(request):
    context = {"employees": Employee.objects.all()}
    return render(request, "employees.html", context)


def vehicles(request):
    context = {"vehicles": Vehicle.objects.all()}
    return render(request, "vehicles.html", context)


def clients(request):
    context = {"Clients": Client.objects.all()}
    return render(request, "clients.html", context)


def tasks(request):
    context = {"tasks": Task.objects.all()}
    return render(request, "tasks.html", context)
