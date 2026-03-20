from django.db import models

class PersonalTrainer(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self): 
        return self.nome

class Membro(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self): 
        return self.nome

class SessaoTreino(models.Model):
    pt = models.ForeignKey(PersonalTrainer, on_delete=models.CASCADE)
    membro = models.ForeignKey(Membro, on_delete=models.CASCADE)
    data = models.DateField()
    hora = models.TimeField()

    class Meta:
        unique_together = ('pt', 'data', 'hora')