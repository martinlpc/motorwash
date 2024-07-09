from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    path("", home, name="home"),  # Se muestran tareas en curso unicamente
    path("about/", about_me, name="about-me"),
    path("employees/", employees, name="employees"),
    path("clients/", clients, name="clients"),
    path("vehicles/", vehicles, name="vehicles"),
    path("tasks/", tasks, name="tasks"),
    # _______ Forms
    # Clients
    path("add/client/", CreateClient.as_view(), name="add-client"),
    path("search/client/", search_clients, name="search-client"),
    path(
        "update/client/<int:pk>/", UpdateClient.as_view(), name="update-client"
    ),
    path(
        "delete/client/<int:pk>/", DeleteClient.as_view(), name="delete-client"
    ),
    # Vehicles
    path("add/vehicle/", CreateVehicle.as_view(), name="add-vehicle"),
    path("search/vehicle/", search_vehicles, name="search-vehicle"),
    path(
        "update/vehicle/<int:pk>/",
        UpdateVehicle.as_view(),
        name="update-vehicle",
    ),
    path(
        "delete/vehicle/<int:pk>/",
        DeleteVehicle.as_view(),
        name="delete-vehicle",
    ),
    # Tasks
    path("add/task/", CreateTask.as_view(), name="add-task"),
    path("search/task/", search_tasks, name="search-task"),
    path("update/task/<int:pk>/", UpdateTask.as_view(), name="update-task"),
    path("delete/task/<int:pk>/", DeleteTask.as_view(), name="delete-task"),
    path("complete/task/", complete_task, name="complete-task"),
    # Employees
    path("add/employee/", CreateEmployee.as_view(), name="add-employee"),
    path("search/employee/", search_employees, name="search-employee"),
    path(
        "update/employee/<int:pk>/",
        UpdateEmployee.as_view(),
        name="update-employee",
    ),
    path(
        "delete/employee/<int:pk>/",
        DeleteEmployee.as_view(),
        name="delete-employee",
    ),
    # Login/logout/register
    path("login/", login_request, name="login"),
    path(
        "logout/",
        LogoutView.as_view(template_name="myapp/logout.html"),
        name="logout",
    ),
    path("register/", register, name="register"),
    # Profile edit / avatar
    path("profile/", edit_profile, name="profile"),
    path("<int:pk>/password/", ChangePassword.as_view(), name="password"),
    path("avatar/", add_avatar, name="add-avatar"),
]
