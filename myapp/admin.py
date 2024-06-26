from django.contrib import admin

# Register your models here.
from .models import *


class ClientAdmin(admin.ModelAdmin):
    list_display = ("DNI", "lastName", "name", "email", "tel")
    list_filter = ("DNI", "lastName", "tel")


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("DNI", "lastName", "name", "tel")
    list_filter = ("lastName",)


class TaskAdmin(admin.ModelAdmin):
    list_display = ("vehicleID", "asignedTo", "description")
    list_filter = ("vehicleID",)


class VehicleAdmin(admin.ModelAdmin):
    list_display = ("plateID", "brand", "brandModel", "ownerDNI")
    list_filter = ("plateID", "brand", "brandModel", "ownerDNI")


admin.site.register(Client, ClientAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Vehicle, VehicleAdmin)
