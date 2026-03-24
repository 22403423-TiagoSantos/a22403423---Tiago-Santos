# models.py
from django.db import models

class Festival(models.Model):
    nome = models.CharField(max_length=100)
    local = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Banda(models.Model):
    nome = models.CharField(max_length=100)
    estilo = models.CharField(max_length=50)

    def __str__(self):
        return self.nome