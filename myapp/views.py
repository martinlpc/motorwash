from django.shortcuts import render
from django.db.models import Q
from .models import *
from .forms import *


def home(request):

    results = []
    if "query" in request.GET:
        results = Task.objects.filter(isCompleted=False)

    return render(request, "active-tasks.html", {"results": results})


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


def find_results_by_model(model: models.Model, query):
    criteria = {
        Client: Q(DNI__icontains=query)
        | Q(last_name__icontains=query)
        | Q(name__icontains=query)
        | Q(DNI__icontains=query)
        | Q(email__icontains=query)
        | Q(tel__icontains=query),
        Vehicle: Q(plate_ID__icontains=query) | Q(owner_DNI__icontains=query),
        Task: Q(vehicle_ID__icontains=query),
        Employee: Q(DNI__icontains=query)
        | Q(name__icontains=query)
        | Q(last_name__icontains=query),
    }

    return model.objects.filter(criteria.get(model))


# Forms
def search_view(request, model: models.Model):
    """
    Realiza búsquedas con el modelo que se le pase como parámetro
    """

    # *     Búsquedas para cada model
    form = SearchForm()
    query = None
    results = []
    modelName = model._meta.model_name.lower() + "s.html"
    if "query" in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data["query"]
            results = find_results_by_model(model, query)
            context = {
                "form": form,
                "query": query,
                "results": results,
                "basehtml": modelName,
            }
    else:
        context = {"form": form, "basehtml": modelName}
    print("results: ", results)
    return render(request, "search-form.html", context)


def search_clients(request):
    return search_view(request, Client)


def search_employees(request):
    return search_view(request, Employee)


def search_vehicles(request):
    return search_view(request, Vehicle)


def search_tasks(request):
    return search_view(request, Task)


# TODO: Ver como integrar un unico form POST adaptable
# TODO: a cada model (usar lógica similar al search)


def add_client_form(request):
    if request.method == "POST":
        myForm = ClientForm(request.POST)
        if myForm.is_valid:
            info = myForm.data
            client = Client(
                DNI=info["DNI"],
                last_name=info["last_name"],
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
                plate_ID=info["plate_ID"],
                vehicle_type=info["vehicle_type"],
                brand=info["brand"],
                brand_model=info["brand_model"],
                owner_DNI=info["owner_DNI"],
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
                asigned_to=info["asigned_to"],
                vehicle_ID=info["vehicle_ID"],
                description=info["description"],
            )
            task.save()
            context = {"tasks": Task.objects.all()}
            return render(request, "tasks.html", context)

    else:
        myForm = TaskForm()

    return render(request, "add-task.html", {"myForm": myForm})


def add_employee_form(request):
    if request.method == "POST":
        myForm = EmployeeForm(request.POST)
        if myForm.is_valid:
            info = myForm.data
            employee = Employee(
                DNI=info["DNI"],
                last_name=info["last_name"],
                name=info["name"],
                tel=info["tel"],
            )
            employee.save()
            context = {"employees": Employee.objects.all()}
            return render(request, "employees.html", context)

    else:
        myForm = EmployeeForm()

    return render(request, "add-employee.html", {"myForm": myForm})
