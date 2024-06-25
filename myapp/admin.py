from django.contrib import admin

# Register your models here.
from .models import *


class ClientAdmin(admin.ModelAdmin):
    list_display = ("dni", "lastName", "name", "vehicles", "email", "tel")
    list_filter = ("dni", "lastName", "tel")


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("dni", "lastName", "name", "tel")
    list_filter = ("lastname",)


class TaskAdmin(admin.ModelAdmin):
    list_display = ("vehicleID", "asignedTo", "tasks")
    list_filter = "vehicleID"


class VehicleAdmin(admin.ModelAdmin):
    list_display = ("plateID", "brand", "brandModel", "ownerDNI")
    list_filter = ("plateID", "brand", "brandModel", "ownderDNI")
