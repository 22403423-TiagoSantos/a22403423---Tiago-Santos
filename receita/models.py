from django.db import models

class Utilizador(models.Model):
    username = models.CharField(max_length=100)
    def __str__(self): 
        return self.username

class Ingrediente(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self): 
        return self.nome

class Receita(models.Model):
    titulo = models.CharField(max_length=100)
    ingredientes = models.ManyToManyField(Ingrediente, related_name='receitas')
    favoritada_por = models.ManyToManyField(Utilizador, related_name='favoritos')
    def __str__(self): 
        return self.titulo