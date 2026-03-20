from django.contrib import admin
from .models import Utilizador, Ingrediente, Receita

class ReceitaAdmin(admin.ModelAdmin):
    list_display = ("titulo",)
    search_fields = ("titulo",)
    filter_horizontal = ("ingredientes", "favoritada_por",)

admin.site.register(Utilizador)
admin.site.register(Ingrediente)
admin.site.register(Receita, ReceitaAdmin)