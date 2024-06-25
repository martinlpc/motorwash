from django.db import models


# Create your models here.
class Client(models.Model):
    DNI = models.CharField(max_length=8)
    lastName = models.CharField(max_length=80)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    tel = models.CharField(max_length=10)
    dateOfBirth = models.DateField()
    dateOfRegister = models.DateField()
    vehicles = []  # Instancias de Vehicle

    def __str__(self):
        return f"{self.lastName}, {self.name}"

    class Meta:
        ordering = ["lastName"]


class Vehicle(models.Model):
    plateID = models.CharField(max_length=7)  # ABC123 / AB123CD
    brand = models.CharField(max_length=50)
    brandModel = models.CharField(max_length=50)
    ownerDNI = models.CharField(max_length=8)

    def __str__(self):
        return f"[{self.plateID}] - {self.brand} {self.brandModel}"

    class Meta:
        ordering = ["brand", "brandModel"]


class Employee(models.Model):
    DNI = models.CharField(max_length=8)
    lastName = models.CharField(max_length=80)
    name = models.CharField(max_length=80)
    tel = models.CharField(max_length=10)


class Task(models.Model):
    asignedTo = models.CharField(max_length=8)  # Por número de DNI
    vehicleID = models.CharField(max_length=7)  # Por patente
    description = models.CharField(max_length=80, default="")
