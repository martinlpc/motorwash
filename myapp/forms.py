from django import forms


class ClientForm(forms.Form):

    name = forms.CharField()
    lastName = forms.CharField()
    DNI = forms.CharField()
    email = forms.EmailField()
    tel = forms.CharField()
