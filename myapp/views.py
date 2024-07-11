from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


def home(request):
    results = Task.objects.filter(is_completed=False)
    return render(request, "myapp/active_tasks.html", {"results": results})


def about_me(request):
    return render(request, "myapp/about_me.html")


@login_required
def employees(request):
    context = {"employees": Employee.objects.all()}
    return render(request, "myapp/employee_list.html", context)


@login_required
def vehicles(request):
    context = {"vehicles": Vehicle.objects.all()}
    return render(request, "myapp/vehicle_list.html", context)


@login_required
def clients(request):
    context = {"clients": Client.objects.all()}
    return render(request, "myapp/client_list.html", context)


@login_required
def tasks(request):
    context = {"tasks": Task.objects.all()}
    return render(request, "myapp/task_list.html", context)


def find_results_by_model(model: models.Model, query):
    if query == "*":
        return model.objects.all()
    else:
        criteria = {
            Client: (
                Q(DNI__icontains=query)
                | Q(last_name__icontains=query)
                | Q(name__icontains=query)
                | Q(DNI__icontains=query)
                | Q(email__icontains=query)
                | Q(tel__icontains=query)
            ),
            Vehicle: (
                Q(plate_ID__icontains=query)
                | Q(owner_DNI__DNI__icontains=query)
            ),
            Task: (Q(vehicle__plate_ID__icontains=query)),
            Employee: (
                Q(DNI__icontains=query)
                | Q(name__icontains=query)
                | Q(last_name__icontains=query)
            ),
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
    modelName = f"myapp/{model._meta.model_name.lower()}_list.html"
    if "query" in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data["query"]
            results = find_results_by_model(model, query)
            # Las primeras tareas a listar serán las últimas que se crearon
            if model == Task:
                results = results.order_by("-id")

            # Si se buscan clientes, se extraen los vehículos asociados
            if model == Client:
                for client in results:
                    vehicles = Vehicle.objects.filter(
                        owner_DNI=client.DNI
                    ).values_list("plate_ID", flat=True)
                    client.plate_IDs = list(vehicles)

            context = {
                "form": form,
                "query": query,
                "results": results,
                "basehtml": modelName,
            }
            return render(request, modelName, context)
    else:
        context = {"form": form, "basehtml": modelName}

    return render(request, "myapp/search_form.html", context)


@login_required
def search_clients(request):
    return search_view(request, Client)


@login_required
def search_employees(request):
    return search_view(request, Employee)


@login_required
def search_vehicles(request):
    return search_view(request, Vehicle)


@login_required
def search_tasks(request):
    return search_view(request, Task)


@login_required
def complete_task(request):
    if request.method == "POST":
        task_id = request.POST.get("id")
        task = get_object_or_404(Task, id=task_id)
        task.is_completed = True
        task.save()
        return redirect("search-task")

    return render(request, "myapp/task_list.html")


# Class Based Views
class CreateClient(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("clients")


class ListClient(LoginRequiredMixin, ListView):
    model = Client


class UpdateClient(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = UpdateClientForm
    success_url = reverse_lazy("clients")


class DeleteClient(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy("clients")


class CreateVehicle(LoginRequiredMixin, CreateView):
    model = Vehicle
    form_class = VehicleForm
    success_url = reverse_lazy("vehicles")


class ListVehicle(LoginRequiredMixin, ListView):
    model = Vehicle


class UpdateVehicle(LoginRequiredMixin, UpdateView):
    model = Vehicle
    form_class = VehicleForm
    success_url = reverse_lazy("vehicles")


class DeleteVehicle(LoginRequiredMixin, DeleteView):
    model = Vehicle
    success_url = reverse_lazy("vehicles")


class CreateEmployee(LoginRequiredMixin, CreateView):
    model = Employee
    form_class = EmployeeForm
    success_url = reverse_lazy("employees")


class ListEmployee(LoginRequiredMixin, ListView):
    model = Employee


class UpdateEmployee(LoginRequiredMixin, UpdateView):
    model = Employee
    form_class = EmployeeForm
    success_url = reverse_lazy("employees")


class DeleteEmployee(LoginRequiredMixin, DeleteView):
    model = Employee
    success_url = reverse_lazy("employees")


class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks")


class ListTask(LoginRequiredMixin, ListView):
    model = Task
    ordering = ["-created"]


class UpdateTask(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks")


class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy("tasks")


# Login / Logout / Register


# * Método con función
def login_request(request):
    if request.method == "POST":
        user_name = request.POST["username"]
        pass_word = request.POST["password"]
        user = authenticate(request, username=user_name, password=pass_word)
        if user is not None:
            login(request, user)
            # Recuperar avatar del usuario
            try:
                avatar = Avatar.objects.get(user=request.user.id).img.url
            except:
                avatar = "/media/avatars/default.png"
            finally:
                request.session["avatar"] = avatar

            return redirect(reverse_lazy("home"))
        else:
            return redirect(reverse_lazy("login"))
    else:
        myForm = AuthenticationForm()

    return render(request, "myapp/login.html", {"form": myForm})


def register(request):
    if request.method == "POST":
        myForm = RegisterForm(request.POST)
        if myForm.is_valid():
            user = myForm.cleaned_data.get("username")
            if User.objects.filter(username=user).exists():
                myForm.add_error(
                    "username", "Nombre de usuario no disponible."
                )
            else:
                myForm.save()
                return redirect(reverse_lazy("home"))

    else:
        myForm = RegisterForm()

    return render(request, "myapp/register.html", {"form": myForm})


@login_required
def edit_profile(request):
    currentUser = request.user
    if request.method == "POST":
        myForm = EditUserForm(request.POST)
        if myForm.is_valid():
            user = User.objects.get(username=currentUser)
            user.email = myForm.cleaned_data.get("email")
            user.first_name = myForm.cleaned_data.get("first_name")
            user.last_name = myForm.cleaned_data.get("last_name")
            user.save()

            return redirect(reverse_lazy("home"))
    else:
        myForm = EditUserForm(instance=currentUser)

    return render(request, "myapp/edit_profile.html", {"form": myForm})


class ChangePassword(LoginRequiredMixin, PasswordChangeView):
    template_name = "myapp/password.html"
    success_url = reverse_lazy("home")


@login_required
def add_avatar(request):
    if request.method == "POST":
        myForm = AvatarForm(request.POST, request.FILES)
        if myForm.is_valid():
            currentUser = User.objects.get(username=request.user)
            newAvatar = myForm.cleaned_data["img"]
            # Borrar avatares antiguos
            oldAvatar = Avatar.objects.filter(user=currentUser)
            if oldAvatar.exists():
                oldAvatar.delete()
            avatar = Avatar(user=currentUser, img=newAvatar)
            avatar.save()
            # Enviar el avatar a home
            img = Avatar.objects.get(user=currentUser).img.url
            request.session["avatar"] = img

            return redirect(reverse_lazy("home"))

    else:
        myForm = AvatarForm()

    return render(request, "myapp/avatar.html", {"form": myForm})
