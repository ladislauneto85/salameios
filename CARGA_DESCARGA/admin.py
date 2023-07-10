from django.contrib import admin
from .models import Carga_Descarga

@admin.register(Carga_Descarga)
class CargaDescargaAdmin(admin.ModelAdmin):
    list_display = ('cad_matricula', 'patente', 'nomeguerra', 'e_mail', 'armamento', 'carreg1', 'carreg2', 'carreg3', 'municao', 'placabalistica', 'observacao', 'data')

