from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),  # Se muestran tareas en curso unicamente
    path("employees/", employees, name="employees"),
    path("clients/", clients, name="clients"),
    path("vehicles/", vehicles, name="vehicles"),
    path("tasks/", tasks, name="tasks"),
    # Forms
    path("add/client/", add_client_form, name="add-client"),
    path("add/vehicle/", add_vehicle_form, name="add-vehicle"),
    path("add/task/", add_task_form, name="add-task"),
    path("add/employee/", add_employee_form, name="add-employee"),
    path("search/clients/", search_clients, name="search-client"),
    path("search/vehicles/", search_vehicles, name="search-vehicle"),
    path("search/tasks/", search_tasks, name="search-task"),
    path("search/employees/", search_employees, name="search-employee"),
]
