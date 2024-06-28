from django import forms


class ClientForm(forms.Form):
    name = forms.CharField(max_length=80, label="Nombre")
    last_name = forms.CharField(max_length=80, label="Apellido")
    DNI = forms.CharField(max_length=8)
    email = forms.EmailField()
    tel = forms.CharField(max_length=10, label="Teléfono")


class VehicleForm(forms.Form):
    plate_ID = forms.CharField(max_length=7, label="Patente")
    types = [
        ("Auto", "Auto"),
        ("SUV", "SUV"),
        ("Camioneta", "Camioneta"),
        ("Moto", "Moto"),
    ]
    vehicle_type = forms.ChoiceField(
        choices=types,
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Tipo de vehículo",
    )
    brand = forms.CharField(max_length=50, label="Marca")
    brand_model = forms.CharField(max_length=50, label="Modelo")
    owner_DNI = forms.CharField(max_length=8, label="DNI del propietario")


class TaskForm(forms.Form):
    asigned_to = forms.CharField(max_length=8, label="DNI empleado")
    vehicle_ID = forms.CharField(max_length=7, label="Patente del vehículo")
    description = forms.CharField(max_length=80, label="Tarea a realizar")


class EmployeeForm(forms.Form):
    name = forms.CharField(max_length=80, label="Nombre")
    last_name = forms.CharField(max_length=80, label="Apellido")
    DNI = forms.CharField(max_length=8)
    tel = forms.CharField(max_length=10, label="Teléfono")


class SearchForm(forms.Form):
    query = forms.CharField(label="Buscar palabra clave", max_length=80)
