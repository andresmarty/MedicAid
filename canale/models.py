from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from datetime import datetime


class ObrasSociales(models.Model):
    obras = models.TextField(blank=True)
    def __str__(self):
        return f"{self.obras}"

class Paciente(models.Model):
    cuil = models.TextField(blank=True)
    nombre = models.TextField(blank=True)
    apellido = models.TextField(blank=True)
    dni = models.TextField(blank=True, null=True)
    fecha_nacimiento = models.DateField(auto_now=False, auto_now_add=False, null=True)
    obra_social = models.ForeignKey(ObrasSociales, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre}"


