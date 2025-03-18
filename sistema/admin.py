from django.contrib import admin

# Importação do módulo models.py
from sistema import models


# Aqui fica o registro do model do Paciente
@admin.register(models.Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'email', 'telefone', 'ativo',)
    list_editable = ('ativo',)
    search_fields = ('id', 'nome', 'email',)


# Aqui fica o registro do model da Especialidade
@admin.register(models.Especialidade)
class EspecialidadeAdmin(admin.ModelAdmin):
   list_display = ('id', 'nome',)

@admin.register(models.Medico)
class MedicoAdmin(admin.ModelAdmin):
   list_display = ('id', 'nome', 'sobrenome','crm', 'ativo')
   list_editable = ('ativo',)
        



   
    

 