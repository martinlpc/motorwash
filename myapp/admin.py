from django.contrib import admin

# Register your models here.
from .models import *


class ClientAdmin(admin.ModelAdmin):
    list_display = ("DNI", "last_name", "name", "email", "tel")
    list_filter = ("DNI", "last_name", "tel")


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("DNI", "last_name", "name", "tel")
    list_filter = ("last_name",)


class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "vehicle",
        "asigned_to",
        "description",
        "is_completed",
    )
    list_filter = (
        "is_completed",
        "vehicle",
    )


class VehicleAdmin(admin.ModelAdmin):
    list_display = ("plate_ID", "brand", "brand_model", "owner_DNI")
    list_filter = ("plate_ID", "brand", "brand_model", "owner_DNI")


admin.site.register(Client, ClientAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Vehicle, VehicleAdmin)
