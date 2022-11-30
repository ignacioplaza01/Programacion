from django.shortcuts import render,redirect
from Tienda.models import Tienda
from Tienda.forms import RegistroTienda

# Create your views here.

def ListaTienda(request):
    tienda = Tienda.objects.all()
    data = {'Tienda':tienda}
    return render(request,'Tienda/tienda.html',data)

def registroTienda(request):
    form = RegistroTienda()
    if request.method == 'POST':
        form = RegistroTienda(request.POST)
        if form.is_valid():
            form.save()
        return ListaTienda(request)    
    data = {'form': form}
    return render(request, 'RegistroTienda/registro.html',data)
    
def EliminarTienda(request,id):
    tienda = Tienda.objects.get(id = id)
    tienda.delete()
    return redirect('/tienda')

def ActualizarTienda(request,id):
    tienda = Tienda.objects.get(id = id)
    form = RegistroTienda(instance=tienda)
    if request.method == 'POST':
        form = RegistroTienda(request.POST, instance=tienda)
        if form.is_valid():
            form.save()
        return ListaTienda(request)    
    data = {'form':form}
    return render(request,'RegistroTienda/registro.html',data)  