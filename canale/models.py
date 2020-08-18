from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from datetime import datetime


class ObrasSociales(models.Model):
    obras = models.TextField(blank=True)
    def __str__(self):
        return f"{self.obras}"

class Paciente(models.Model):
    cuil = models.CharField(max_length=64, null=False)
    nombre = models.CharField(max_length=64, null=False)
    apellido = models.CharField(max_length=64, null=False)
    dni = models.CharField(max_length=64, null=True)
    fecha_nacimiento = models.DateField(auto_now=False, auto_now_add=False, null=True)
    obra_social = models.ForeignKey(ObrasSociales, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre}"

class Practicas(models.Model):
    #fecha = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    tipo = models.CharField(max_length=64, null=False)
    estado = models.CharField(max_length=64, null=False)
    obra_social = models.ForeignKey(ObrasSociales, blank=True, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tipo}"
