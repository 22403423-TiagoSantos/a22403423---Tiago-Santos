from django.contrib import admin
from .models import Genero, Banda, Festival

class GeneroAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)

class BandaAdmin(admin.ModelAdmin):
    list_display = ("nome", "genero")
    search_fields = ("nome",)

class FestivalAdmin(admin.ModelAdmin):
    list_display = ("nome", "localizacao")
    search_fields = ("nome",)
    filter_horizontal = ("bandas",) 

admin.site.register(Genero, GeneroAdmin)
admin.site.register(Banda, BandaAdmin)
admin.site.register(Festival, FestivalAdmin)