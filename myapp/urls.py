from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("employees/", employees, name="employees"),
    path("clients/", clients, name="clients"),
    path("vehicles/", vehicles, name="vehicles"),
    path("tasks/", tasks, name="tasks"),
]
