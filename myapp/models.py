from django.db import models
from django.utils import timezone


# Create your models here.
class Client(models.Model):
    DNI = models.CharField(max_length=8)
    last_name = models.CharField(max_length=80)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    tel = models.CharField(max_length=10)

    def __str__(self):
        return f"[DNI {self.DNI}] - {self.last_name}, {self.name} - {self.email} - Tel: {self.tel}"

    class Meta:
        ordering = ["last_name"]


class Vehicle(models.Model):
    plate_ID = models.CharField(max_length=7, unique=True)  # ABC123 / AB123CD
    vehicle_type = models.CharField(max_length=15)
    brand = models.CharField(max_length=50)
    brand_model = models.CharField(max_length=50)
    owner_DNI = models.CharField(max_length=8)

    def __str__(self):
        return f"[{self.plate_ID}] [{self.vehicle_type}] - {self.brand} {self.brand_model} - DNI propietario/a: {self.owner_DNI}"

    class Meta:
        ordering = ["brand", "brand_model"]


class Employee(models.Model):
    DNI = models.CharField(max_length=8)
    last_name = models.CharField(max_length=80)
    name = models.CharField(max_length=80)
    tel = models.CharField(max_length=10)

    def __str__(self):
        return f"[DNI {self.DNI}] - {self.last_name}, {self.name} - Tel: {self.tel}"


class Task(models.Model):
    created = models.DateTimeField(default=timezone.now)
    asigned_to = models.CharField(max_length=8)  # Por número de DNI
    vehicle = models.ForeignKey(
        Vehicle, to_field="plate_ID", on_delete=models.SET_NULL, null=True
    )  # Por patente
    description = models.CharField(max_length=80, default="")
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"[{self.created}] {self.vehicle_ID} asignado a {self.asigned_to}: {self.description}"

    def formatted_created(self):
        return self.created.strftime("%d/%m/%Y %H:%M:%S")
