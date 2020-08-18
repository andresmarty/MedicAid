from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.forms import ModelForm, Textarea, TextInput, NumberInput, DateInput, Select
from .models import Paciente, ObrasSociales, Practicas
from django import forms
from django.contrib import messages
# Create your views here.


class DateInput(forms.DateInput):
    input_type = 'date'

class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = ['cuil', 'nombre', 'apellido', 'dni', 'fecha_nacimiento', 'obra_social']
        widgets = {
            'cuil' : TextInput(attrs={'class': 'form-control input'}),
            'nombre' : TextInput(attrs={'class': 'form-control input'}),
            'apellido' : TextInput(attrs={'class': 'form-control input'}),
            'dni' : TextInput(attrs={'class': 'form-control input'}),
            'fecha_nacimiento' : DateInput(format=('%d-%m-%Y'), attrs={'class':'form-control input'}),
            'obra_social': Select(attrs={'class': 'custom-select form-control select'})
        }
        labels = {
            'cuil' : 'Insertar Cuil',
            'nombre' : 'Insertar Nombre',
            'apellido' : 'Insertar Apellido',
            'dni' : 'Insertar DNI',
            'fecha_nacimiento' : 'Insertar Fecha de Nacimiento',
            'obra_social': 'Seleccionar Obra Social'
        }

class PracticasForm(ModelForm):
    class Meta:
        model = Practicas
        fields = ['tipo', 'estado', 'obra_social']
        widgets = {
            'tipo' : TextInput(attrs={'class': 'form-control input'}),
            'estado' : TextInput(attrs={'class': 'form-control input'}),
            'obra_social' : Select(attrs={'class': 'custom-select form-control select'}),
        }

def index(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            paciente = Paciente()
            paciente.cuil = form.cleaned_data["cuil"]
            paciente.nombre = form.cleaned_data["nombre"]
            paciente.apellido = form.cleaned_data["apellido"]
            paciente.dni = form.cleaned_data["dni"]
            paciente.fecha_nacimiento = form.cleaned_data["fecha_nacimiento"]
            paciente.obra_social = form.cleaned_data["obra_social"]
            paciente.save()
            messages.add_message(request, messages.SUCCESS, 'Pacient Added.')
            return HttpResponseRedirect(reverse("index"))


    return render(request, "canale/index.html", {
        'form': PacienteForm()
    })
            
def practicas(request):
    if request.method == 'POST':
        form = PracticasForm(request.POST)
        if form.is_valid():
            practicas = Practicas()
            practicas.estado = form.cleaned_data["estado"]
            practicas.obra_social = form.cleaned_data["obra_social"]
            practicas.save()
            messages.add_message(request, messages.SUCCESS, 'Practica Added.')
            return HttpResponseRedirect(reverse("index"))
    
    return render (request, "canale/practicas.html", {
        'form': PracticasForm()
    })

