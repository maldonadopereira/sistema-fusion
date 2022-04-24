from django.contrib import admin

from core.models import Servico, Cargo, Funcionario, Feature


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'criado')
    list_display_links = ('nome',)

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cargo', 'criado')
    list_display_links = ('cargo',)

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'criado')
    list_display_links = ('nome',)

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'criado')
    list_display_links = ('nome',)