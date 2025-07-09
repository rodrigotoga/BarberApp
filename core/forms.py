from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Cliente, Corte

class ClienteRegisterForm(UserCreationForm):
    email = forms.EmailField()
    telefone = forms.CharField(max_length=20)

    class Meta:
        model = Cliente
        fields = ['username', 'email', 'telefone', 'password1', 'password2']

class CorteForm(forms.ModelForm):
    class Meta:
        model = Corte
        fields = ['data', 'hora', 'valor']