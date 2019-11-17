from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from datetime import datetime,date, time,timezone
from hostal.models import Cliente, Comedor2, Comedor

class AgregarClienteForm(UserCreationForm):

    email = forms.CharField(max_length=50, 
    widget=forms.EmailInput(attrs={'class': 'form-control',
    'placeholder':'ejemplo@ejemplo.cl'}))
    username = forms.CharField(max_length=100, 
    widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'bcordova', 'label':'Usuario'}))
    first_name = forms.CharField(max_length=100, 
    widget=forms.TextInput(attrs={'class': 'form-control',
    'placeholder':'Bruno Cordova'}))
    run = forms.CharField(max_length=12, 
    widget=forms.TextInput(attrs={'class': 'form-control',
    'placeholder':'13.988.666-6'}))
    empresa = forms.CharField(max_length=100, 
    widget=forms.TextInput(attrs={'class': 'form-control',
    'placeholder':'Duoc UC'}))
    cargo = forms.CharField(max_length=100, 
    widget=forms.TextInput(attrs={'class': 'form-control',
    'placeholder':'Ingeniero Informatico'}))
    direccion = forms.CharField(max_length=100, 
    widget=forms.TextInput(attrs={'class': 'form-control',
    'placeholder':'Miraflores #443'}))
    telefono = forms.CharField(max_length=100, 
    widget=forms.TextInput(attrs={'class': 'form-control',
    'placeholder':'+56 9907012'})) 
    ciudad = forms.CharField(max_length=50, 
    widget=forms.TextInput(attrs={'class': 'form-control',
    'id':'comunas' , 'placeholder':'Valparaiso'}))

    class Meta:
        model = User
        fields = ('username' , 'password1', 'password2' , 'email' , 'first_name', 'empresa', 'cargo', 'direccion', 'telefono', 
        'ciudad', 'run',  )


class AgregarComedorForm (forms.ModelForm):
    fecha = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control', 'type':'date'
        })
    )
    class Meta:
        model = Comedor
        fields = ('nombre', 'fecha', 'entrada', 'plato', 
        'postre', 'precio', )



class AgregarPlatosForm(forms.ModelForm):
    
   

    class Meta:
        model = Comedor2
        fields = ('nombreplato', 'descripcion', 'precio', 'servicio', )


      




