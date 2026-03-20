from django.contrib import admin
from .models import Professor, Turma, Aluno

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)

class TurmaAdmin(admin.ModelAdmin):
    list_display = ("nome", "professor",)
    search_fields = ("nome",)

class AlunoAdmin(admin.ModelAdmin):
    list_display = ("nome", "turma",)
    ordering = ("nome",)
    search_fields = ("nome",)

admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Turma, TurmaAdmin)
admin.site.register(Aluno, AlunoAdmin)