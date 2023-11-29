from django.shortcuts import render, redirect
from Zurita_T_IEI170_app.models import Reserva
from Zurita_T_IEI170_app.forms import ReservaForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def listar_reserva(request):
    reservas = Reserva.objects.all()
    data = {'reservas': reservas}
    return render(request, 'reservas.html', data)

def agregar_reserva(request):
    form = ReservaForm()

    if request.method == "POST":
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    
    data = {'form': form}
    return render(request, 'agregar_reserva.html', data)

def eliminar_reserva(request, id):
    reserva = Reserva.objects.get(id=id)
    reserva.delete()
    return redirect('/reservas')


def modificar_reserva(request, id):
    reserva = Reserva.objects.get(id=id)
    form = ReservaForm(instance=reserva)

    if request.method == "POST":
        form = ReservaForm(request.POST, instance=reserva)
        if (form.is_valid()):
            form.save()
        return redirect('/reservas')
        
    data = {'form': form}
    return render(request, 'agregar_reserva.html',data)


