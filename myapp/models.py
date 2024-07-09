from typing import Any
from django.db import models
from django.utils import timezone
from django.utils.deconstruct import deconstructible
from django.contrib.auth.models import User
import os


# Create your models here.
class Client(models.Model):
    DNI = models.CharField(max_length=8, unique=True)
    last_name = models.CharField(max_length=80)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    tel = models.CharField(max_length=10)

    def __str__(self):
        return f"[DNI {self.DNI}] - {self.last_name}, {self.name} - {self.email} - Tel: {self.tel}"

    class Meta:
        ordering = ["last_name"]


class Vehicle(models.Model):
    AUTOMOVIL = "Automóvil"
    MOTO = "Moto"
    CAMIONETA = "Camioneta"
    SUV = "SUV"
    CAMION = "Camión"
    OTRO = "Otro"

    VEHICLE_TYPE_CHOICES = [
        (AUTOMOVIL, "Automovil"),
        (MOTO, "Moto"),
        (CAMIONETA, "Camioneta"),
        (SUV, "SUV"),
        (CAMION, "Camión"),
        (OTRO, "Otro"),
    ]

    plate_ID = models.CharField(max_length=7, unique=True)  # ABC123 / AB123CD
    vehicle_type = models.CharField(
        max_length=15, choices=VEHICLE_TYPE_CHOICES, default=AUTOMOVIL
    )
    brand = models.CharField(max_length=50)
    brand_model = models.CharField(max_length=50)
    owner_DNI = models.ForeignKey(
        Client,
        to_field="DNI",
        null=False,
        on_delete=models.CASCADE,
        related_name="vehicles",
    )

    def __str__(self):
        return f"[{self.plate_ID}] [{self.vehicle_type}] - {self.brand} {self.brand_model} - DNI propietario/a: {self.owner_DNI}"

    class Meta:
        ordering = ["brand", "brand_model"]


class Employee(models.Model):
    DNI = models.CharField(max_length=8, unique=True)
    last_name = models.CharField(max_length=80)
    name = models.CharField(max_length=80)
    tel = models.CharField(max_length=10)

    def __str__(self):
        return f"[DNI {self.DNI}] - {self.last_name}, {self.name} - Tel: {self.tel}"


class Task(models.Model):
    created = models.DateTimeField(default=timezone.now)
    asigned_to = models.ForeignKey(
        Employee, to_field="DNI", null=True, on_delete=models.SET_NULL
    )  # Por número de DNI
    vehicle = models.ForeignKey(
        Vehicle, to_field="plate_ID", on_delete=models.SET_NULL, null=True
    )  # Por patente
    description = models.CharField(max_length=80, default="")
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"[{self.created}] {self.vehicle} asignado a {self.asigned_to}: {self.description}"

    def formatted_created(self):
        return self.created.strftime("%d/%m/%Y %H:%M:%S")


@deconstructible
class AvatarPath(object):
    """
    Clase para definir correctamente el filename de un avatar en formato '[user.id]_[user.username]'
    """

    def __call__(self, instance, filename):
        extension = filename.split(".")[-1]
        filename = f"{instance.user.id}_{instance.user.username}.{extension}"
        return os.path.join("avatars", filename)


class Avatar(models.Model):
    img = models.ImageField(upload_to=AvatarPath())
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.img}"
