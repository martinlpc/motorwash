from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    path("", home, name="home"),  # Se muestran tareas en curso unicamente
    path("employees/", employees, name="employees"),
    path("clients/", clients, name="clients"),
    path("vehicles/", vehicles, name="vehicles"),
    path("tasks/", tasks, name="tasks"),
    # _______ Forms
    # Clients
    path("add/client/", CreateClient.as_view(), name="add-client"),
    path("search/client/", ListClient.as_view(), name="search-client"),
    path("update/client/", UpdateClient.as_view(), name="update-client"),
    path("delete/client/", DeleteClient.as_view(), name="delete-client"),
    # Vehicles
    path("add/vehicle/", CreateVehicle.as_view(), name="add-vehicle"),
    path("search/vehicle/", ListVehicle.as_view(), name="search-vehicle"),
    path("update/vehicle/", UpdateVehicle.as_view(), name="update-vehicle"),
    path("delete/vehicle/", DeleteVehicle.as_view(), name="delete-vehicle"),
    # Tasks
    path("add/task/", CreateTask.as_view, name="add-task"),
    path("search/task/", ListTask.as_view(), name="search-task"),
    path("update/task/", UpdateTask.as_view(), name="update-task"),
    path("delete/task/", DeleteTask.as_view(), name="delete-task"),
    # Employees
    path("add/employee/", CreateEmployee.as_view(), name="add-employee"),
    path("search/employee/", ListEmployee.as_view(), name="search-employee"),
    path("update/employee/", UpdateEmployee.as_view(), name="update-employee"),
    path("delete/employee/", DeleteEmployee.as_view(), name="delete-employee"),
    # Login/logout/register
    path("login/", login_request, name="login"),
    path(
        "logout/",
        LogoutView.as_view(template_name="logout.html"),
        name="logout",
    ),
    path("register/", register, name="register"),
]
