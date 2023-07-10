from django.contrib import admin
from .models import CadastroArma, Carregador_1, Carregador_2, Carregador_3, CadastroColete

@admin.register(CadastroArma)
class CadastroBelicoAdmin(admin.ModelAdmin):
    list_display = ('numero_serie', 'tipo', 'modelo')

@admin.register(Carregador_1)
class CadastroBelicoAdmin(admin.ModelAdmin):
    list_display = ('num_serie_1', 'qtd_carreg_1')

@admin.register(Carregador_2)
class CadastroBelicoAdmin(admin.ModelAdmin):
    list_display = ('num_serie_2', 'qtd_carreg_2')

@admin.register(Carregador_3)
class CadastroBelicoAdmin(admin.ModelAdmin):
    list_display = ('num_serie_3', 'qtd_carreg_3')

@admin.register(CadastroColete)
class CadastroBelicoAdmin(admin.ModelAdmin):
    list_display = ('numerocad', 'tamanho', 'fabricante')
