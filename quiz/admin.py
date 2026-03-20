from django.contrib import admin
from .models import Quiz, Pergunta, Resposta

class RespostaInline(admin.TabularInline):
    model = Resposta
    extra = 4

class PerguntaAdmin(admin.ModelAdmin):
    list_display = ("enunciado", "quiz",)
    list_filter = ("quiz",)
    search_fields = ("enunciado",)
    inlines = [RespostaInline]

class QuizAdmin(admin.ModelAdmin):
    list_display = ("titulo",)
    search_fields = ("titulo",)

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Pergunta, PerguntaAdmin)
admin.site.register(Resposta)