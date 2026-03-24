# admin.py
from django.contrib import admin
from .models import Festival, Banda

@admin.register(Festival)
class FestivalAdmin(admin.ModelAdmin):
    list_display = ("nome", "local")
    search_fields = ("nome",)


@admin.register(Banda)
class BandaAdmin(admin.ModelAdmin):
    list_display = ("nome", "estilo")
    search_fields = ("nome",)