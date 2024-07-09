from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import *


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["DNI", "last_name", "name", "email", "tel"]
        labels = {
            "DNI": "DNI",
            "last_name": "Apellido",
            "name": "Nombre(s)",
            "email": "Email",
            "tel": "Teléfono de contacto",
        }


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = [
            "plate_ID",
            "vehicle_type",
            "brand",
            "brand_model",
            "owner_DNI",
        ]
        labels = {
            "plate_ID": "Patente del vehículo",
            "vehicle_type": "Tipo de vehículo",
            "brand": "Marca",
            "brand_model": "Modelo",
            "owner_DNI": "DNI del dueño(a)",
        }


class UpdateVehicleForm(forms.ModelForm):
    # No se permite modificar la patente
    # Hacemos que este campo sea read-only en el widget HTML
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["plate_ID"].widget.attrs["readonly"] = True

    class Meta:
        model = Vehicle
        fields = [
            "plate_ID",
            "vehicle_type",
            "brand",
            "brand_model",
            "owner_DNI",
        ]
        labels = {
            "plate_ID": "Patente del vehículo",
            "vehicle_type": "Tipo de vehículo",
            "brand": "Marca",
            "brand_model": "Modelo",
            "owner_DNI": "DNI del dueño(a)",
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["asigned_to", "vehicle", "description"]
        labels = {
            "asigned_to": "Asignado a",
            "vehicle": "Vehículo",
            "description": "Trabajo a realizar",
        }


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ["DNI", "last_name", "name", "tel"]
        labels = {
            "DNI": "DNI",
            "last_name": "Apellido",
            "name": "Nombre(s)",
            "tel": "Teléfono de contacto",
        }


class SearchForm(forms.Form):
    query = forms.CharField(
        label="Buscar palabra clave (ingrese * para ver todos los registros)",
        max_length=80,
    )


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
