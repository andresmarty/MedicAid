from django.contrib import admin

from .models import Paciente, ObrasSociales, Practicas

# Register your models here.
admin.site.register(Paciente)
admin.site.register(ObrasSociales)
admin.site.register(Practicas)