from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


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


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Repita contraseña", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        ]


class EditUserForm(UserChangeForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label="Nombre", required=True, max_length=80)
    last_name = forms.CharField(label="Apellido", required=True, max_length=80)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]


class AvatarForm(forms.Form):
    img = forms.ImageField(required=True, label="Nuevo avatar")
