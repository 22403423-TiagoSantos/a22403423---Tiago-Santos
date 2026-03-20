from django.contrib import admin
from .models import Cliente, Morada, Categoria, Produto, Pedido, ItemPedido

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco", "categoria",)
    list_filter = ("categoria",)
    search_fields = ("nome",)

class PedidoAdmin(admin.ModelAdmin):
    list_display = ("id", "cliente", "data_pedido",)
    ordering = ("-data_pedido",)

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register([Cliente, Morada, Categoria, ItemPedido])