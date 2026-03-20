from django.contrib import admin
from .models import PersonalTrainer, Membro, SessaoTreino

class PersonalTrainerAdmin(admin.ModelAdmin):
    list_display = ("nome",)

class MembroAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)

class SessaoTreinoAdmin(admin.ModelAdmin):
    list_display = ("data", "hora", "pt", "membro",)
    ordering = ("data", "hora",)
    search_fields = ("pt__nome", "membro__nome",)

admin.site.register(PersonalTrainer, PersonalTrainerAdmin)
admin.site.register(Membro, MembroAdmin)
admin.site.register(SessaoTreino, SessaoTreinoAdmin)