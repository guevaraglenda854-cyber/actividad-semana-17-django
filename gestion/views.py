from django.shortcuts import render, redirect, get_object_or_404
from .models import Dueno, Mascota, Consulta
from .forms import DuenoForm, MascotaForm, ConsultaForm


def inicio(request):
    return render(request, "gestion/inicio.html", {
        "duenos": Dueno.objects.all(),
        "mascotas": Mascota.objects.select_related("dueno").all(),
        "consultas": Consulta.objects.select_related("mascota", "mascota__dueno").all(),
    })


def crear_dueno(request):
    form = DuenoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("inicio")
    return render(request, "gestion/formulario.html", {"form": form, "titulo": "Registrar Dueño"})


def editar_dueno(request, pk):
    dueno = get_object_or_404(Dueno, pk=pk)
    form = DuenoForm(request.POST or None, instance=dueno)
    if form.is_valid():
        form.save()
        return redirect("inicio")
    return render(request, "gestion/formulario.html", {"form": form, "titulo": "Editar Dueño"})


def eliminar_dueno(request, pk):
    dueno = get_object_or_404(Dueno, pk=pk)
    if request.method == "POST":
        dueno.delete()
        return redirect("inicio")
    return render(request, "gestion/confirmar_eliminar.html", {"objeto": dueno})


def crear_mascota(request):
    form = MascotaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("inicio")
    return render(request, "gestion/formulario.html", {"form": form, "titulo": "Registrar Mascota"})


def editar_mascota(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    form = MascotaForm(request.POST or None, instance=mascota)
    if form.is_valid():
        form.save()
        return redirect("inicio")
    return render(request, "gestion/formulario.html", {"form": form, "titulo": "Editar Mascota"})


def eliminar_mascota(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    if request.method == "POST":
        mascota.delete()
        return redirect("inicio")
    return render(request, "gestion/confirmar_eliminar.html", {"objeto": mascota})


def crear_consulta(request):
    form = ConsultaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("inicio")
    return render(request, "gestion/formulario.html", {"form": form, "titulo": "Registrar Consulta"})


def editar_consulta(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)
    form = ConsultaForm(request.POST or None, instance=consulta)
    if form.is_valid():
        form.save()
        return redirect("inicio")
    return render(request, "gestion/formulario.html", {"form": form, "titulo": "Editar Consulta"})


def eliminar_consulta(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)
    if request.method == "POST":
        consulta.delete()
        return redirect("inicio")
    return render(request, "gestion/confirmar_eliminar.html", {"objeto": consulta})