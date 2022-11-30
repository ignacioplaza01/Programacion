from django.shortcuts import render, redirect
from django.http import HttpResponse
from Ropa.forms import RegistroRopa
from Ropa.models import Ropa

# Create your views here.



def Ropas(request):
    ropa = Ropa.objects.all()
    data = {'Ropa':ropa}
    return render(request,'Lista/ListaRopa.html',data)

def listadoropa(request):
    form = RegistroRopa()
    if request.method == 'POST':
        form = RegistroRopa(request.POST)
        if form.is_valid():
            form.save()
        return Ropas(request)    
    data = {'form': form}
    return render(request, 'Registrar/Registroropa.html',data)
    
def EliminarR(request,id):
    ropa = Ropa.objects.get(id = id)
    ropa.delete()
    return redirect('/ropa')

def Actualizar(request,id):
    ropa = Ropa.objects.get(id = id)
    form = RegistroRopa(instance=ropa)
    if request.method == 'POST':
        form = RegistroRopa(request.POST, instance=ropa)
        if form.is_valid():
            form.save()
        return Ropas(request)    
    data = {'form':form}
    return render(request,'Registrar/Registroropa.html',data)  