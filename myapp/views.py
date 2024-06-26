from django.shortcuts import render
from .models import *
from .forms import *


def home(request):
    return render(request, "index.html")


def employees(request):
    context = {"employees": Employee.objects.all()}
    return render(request, "employees.html", context)


def vehicles(request):
    context = {"vehicles": Vehicle.objects.all()}
    return render(request, "vehicles.html", context)


def clients(request):
    context = {"clients": Client.objects.all()}
    return render(request, "clients.html", context)


def tasks(request):
    context = {"tasks": Task.objects.all()}
    return render(request, "tasks.html", context)


def add_client_form(request):

    if request.method == "POST":

        myForm = ClientForm(request.POST)
        if myForm.is_valid:

            info = myForm.data
            client = Client(
                DNI=info["DNI"],
                lastName=info["lastName"],
                name=info["name"],
                email=info["email"],
                tel=info["tel"],
            )
            client.save()

            return render(request, "index.html")

    else:
        myForm = ClientForm()

    return render(request, "add-client.html", {"myForm": myForm})
