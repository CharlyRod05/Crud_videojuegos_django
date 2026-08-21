from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Videojuego
from .forms import VideojuegoForm


def lista_videojuegos(request):
    videojuegos = Videojuego.objects.all()
    return render(request, 'videojuegos/lista.html', {'videojuegos': videojuegos})


def crear_videojuego(request):
    if request.method == 'POST':
        form = VideojuegoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('videojuegos:lista')
    else:
        form = VideojuegoForm()
    return render(request, 'videojuegos/crear.html', {'form': form})


def editar_videojuego(request, pk):
    videojuego = get_object_or_404(Videojuego, pk=pk)
    if request.method == 'POST':
        form = VideojuegoForm(request.POST, instance=videojuego)
        if form.is_valid():
            form.save()
            return redirect('videojuegos:lista')
    else:
        form = VideojuegoForm(instance=videojuego)
    return render(request, 'videojuegos/editar.html', {'form': form})


def eliminar_videojuego(request, pk):
    videojuego = get_object_or_404(Videojuego, pk=pk)
    if request.method == 'POST':
        videojuego.delete()
        return redirect('videojuegos:lista')
    return render(request, 'videojuegos/eliminar.html', {'videojuego': videojuego})