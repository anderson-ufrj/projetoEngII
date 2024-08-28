from django.contrib import admin
from .models import *

# Registro das classes no admin do Django

admin.site.register(UF)
admin.site.register(Cidade)
admin.site.register(Ingrediente)
admin.site.register(TipoIngrediente)
admin.site.register(Servico)
admin.site.register(TipoServico)
admin.site.register(Prato)
admin.site.register(TipoPrato)
admin.site.register(PedidoCliente)
admin.site.register(PedidoGarcom)
admin.site.register(Fornecedor)
admin.site.register(OrdemProducao)
admin.site.register(Entrega)
admin.site.register(Venda)
admin.site.register(ContatoCliente)
admin.site.register(Garcom)

