from django import forms


class ClientForm(forms.Form):
    name = forms.CharField(max_length=80, label="Nombre")
    lastName = forms.CharField(max_length=80, label="Apellido")
    DNI = forms.CharField(max_length=8)
    email = forms.EmailField()
    tel = forms.CharField(max_length=10, label="Teléfono")


class VehicleForm(forms.Form):
    vehicleID = forms.CharField(max_length=7, label="Patente")
    types = [
        ("Auto", "Auto"),
        ("SUV", "SUV"),
        ("Camioneta", "Camioneta"),
        ("Moto", "Moto"),
    ]
    vehicleType = forms.ChoiceField(
        choices=types,
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Tipo de vehículo",
    )
    brand = forms.CharField(max_length=50, label="Marca")
    brandModel = forms.CharField(max_length=50, label="Modelo")
    ownerDNI = forms.CharField(max_length=8, label="DNI del propietario")


class TaskForm(forms.Form):
    asignedTo = forms.CharField(max_length=8, label="DNI empleado")
    vehicleID = forms.CharField(max_length=7, label="Patente del vehículo")
    description = forms.CharField(max_length=80, label="Tarea a realizar")


class EmployeeForm(forms.Form):
    name = forms.CharField(max_length=80, label="Nombre")
    lastName = forms.CharField(max_length=80, label="Apellido")
    DNI = forms.CharField(max_length=8)
    tel = forms.CharField(max_length=10, label="Teléfono")


class SearchForm(forms.Form):
    query = forms.CharField(label="Buscar", max_length=80)
