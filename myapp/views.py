from django.shortcuts import render
from django.db.models import Q
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


# Forms
def search_view(request, model):
    """
    Realiza búsquedas con el modelo que se le pase como parámetro
    """
    form = SearchForm()
    query = None
    results = []
    if "query" in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data["query"]
            results = model.objects.filter(
                Q(name__icontains=query)
                | Q(lastName__icontains=query)
                | Q(vehicleID__icontains=query)
                | Q(DNI__icontains=query)
                | Q(ownerDNI__icontains=query)
            )
            context = {"form": form, "query": query, "results": results}

    return render(request, "search-form.html", context)


def search_clients(request):
    return search_view(request, Client)


def search_employees(request):
    return search_view(request, Employee)


def search_vehicles(request):
    return search_view(request, Vehicle)


def search_tasks(request):
    return search_view(request, Task)


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
            context = {"clients": Client.objects.all()}
            return render(request, "clients.html", context)

    else:
        myForm = ClientForm()

    return render(request, "add-client.html", {"myForm": myForm})


def add_vehicle_form(request):
    if request.method == "POST":
        myForm = VehicleForm(request.POST)
        if myForm.is_valid:
            info = myForm.data
            vehicle = Vehicle(
                plateID=info["plateID"],
                vehicleType=info["vehicleType"],
                brand=info["brand"],
                brandModel=info["brandModel"],
                ownerDNI=info["ownerDNI"],
            )
            vehicle.save()
            context = {"vehicles": Vehicle.objects.all()}
            return render(request, "vehicles.html", context)

    else:
        myForm = VehicleForm()

    return render(request, "add-vehicle.html", {"myForm": myForm})


def add_task_form(request):
    if request.method == "POST":
        myForm = TaskForm(request.POST)
        if myForm.is_valid:
            info = myForm.data
            task = Task(
                asignedTo=info["asignedTo"],
                vehicleID=info["vehicleID"],
                description=info["description"],
            )
            task.save()
            context = {"tasks": Task.objects.all()}
            return render(request, "tasks.html", context)

    else:
        myForm = TaskForm()

    return render(request, "add-task.html", {"myForm": myForm})
