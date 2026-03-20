from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self): 
        return self.nome

class Morada(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE, related_name='perfil_morada')
    rua = models.CharField(max_length=200)
    cidade = models.CharField(max_length=100)

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self): 
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    def __str__(self): 
        return self.nome

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_pedido = models.DateTimeField(auto_now_add=True)

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='items')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)