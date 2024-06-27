from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("employees/", employees, name="employees"),
    path("clients/", clients, name="clients"),
    path("vehicles/", vehicles, name="vehicles"),
    path("tasks/", tasks, name="tasks"),
    # Forms
    path("add/client/", add_client_form, name="add-clients"),
    path("add/vehicle/", add_vehicle_form, name="add-vehicles"),
    path("add/task/", add_task_form, name="add-tasks"),
    path("add/employee/", add_employee_form, name="add-employees"),
    path("search/clients/", search_clients, name="search-clients"),
    path("search/vehicles/", search_vehicles, name="search-vehicles"),
    path("search/tasks/", search_tasks, name="search-tasks"),
    path("search/employees/", search_employees, name="search-employees"),
]
