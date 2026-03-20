from django.db import models

class Quiz(models.Model):
    titulo = models.CharField(max_length=100)
    
    def __str__(self):
        return self.titulo

class Pergunta(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='perguntas')
    enunciado = models.TextField()

    def __str__(self):
        return self.enunciado

class Resposta(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE, related_name='respostas')
    texto = models.CharField(max_length=255)
    e_correta = models.BooleanField(default=False)

    def __str__(self):
        return self.texto