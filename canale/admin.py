from django.contrib import admin

from .models import Paciente, ObrasSociales

# Register your models here.
admin.site.register(Paciente)
admin.site.register(ObrasSociales)