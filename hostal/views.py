from django.shortcuts import render, redirect
from hostal.forms import AgregarClienteForm,AgregarComedorForm,AgregarPlatosForm
from hostal.models import Cliente, Comedor, Comedor2
from django.contrib import messages


def home(request):

    return render(request,"home.html")



def login(request):

    return render(request, "login.html")


def cliente_OK(request):

    return render(request, 'clienteregistrado.html')

def Comedor_OK(request):

    return render(request,'comedorOK.html')



def Comedor_OK2(request):

    return render(request,'comedorOK2.html')


def cliente(request):

    if request.method == 'POST':
        form = AgregarClienteForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db() 
            user.cliente.email = form.cleaned_data.get('email') 
            user.cliente.first_name = form.cleaned_data.get('first_name')
            user.cliente.empresa = form.cleaned_data.get('empresa')
            user.cliente.cargo = form.cleaned_data.get('cargo')
            user.cliente.direccion  = form.cleaned_data.get('direccion')
            user.cliente.telefono = form.cleaned_data.get('telefono')
            user.cliente.ciudad = form.cleaned_data.get('ciudad')
            user.cliente.run = form.cleaned_data.get('run')
            user.save()
            messages.success(request, "Cliente Agregado")

            return redirect('clienteOK')
    else:
        form = AgregarClienteForm()
    return render(request, 'registro.html', {'form': form})    


def comedor(request):

    return render(request,'comedor.html')

def comedorMenu(request):

    if request.method == 'POST':
        form = AgregarComedorForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            
            return redirect ('comedorOK')
    else:
        form = AgregarComedorForm()
    return render(request, 'comedorMenu.html', {'form': form})  


def comedorPlatos(request):

    if request.method == 'POST':
        form = AgregarPlatosForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            
            return redirect ('comedorOK2')
    else:
        form = AgregarPlatosForm()
    return render(request, 'comedorPlatos.html', {'form': form})   





