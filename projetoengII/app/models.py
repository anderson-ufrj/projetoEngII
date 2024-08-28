from django.db import models

class UF(models.Model):
    sigla = models.CharField(max_length=2)

    class Meta:
        verbose_name_plural = 'UFs'

    def __str__(self):
        return self.sigla

class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    uf = models.ForeignKey(UF, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Cidades'

    def __str__(self):
        return self.nome

class TipoIngrediente(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Tipos de Ingredientes'

    def __str__(self):
        return self.nome

class Ingrediente(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.ForeignKey(TipoIngrediente, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Ingredientes'

    def __str__(self):
        return self.nome

class TipoServico(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Tipos de Serviços'

    def __str__(self):
        return self.nome

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.ForeignKey(TipoServico, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.nome

class TipoPrato(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Tipos de Pratos'

    def __str__(self):
        return self.nome

class Prato(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.ForeignKey(TipoPrato, on_delete=models.CASCADE)
    

    class Meta:
        verbose_name_plural = 'Pratos'

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    contato = models.CharField(max_length=100)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Fornecedores'

    def __str__(self):
        return self.nome

class Garcom(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=20)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Garçons'

    def __str__(self):
        return self.nome

class PedidoCliente(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    pratos = models.ManyToManyField(Prato)
    status = models.CharField(max_length=100)
    data_pedido = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Pedidos de Clientes'

    def __str__(self):
        return f"Pedido Cliente {self.id} - {self.cliente.nome}"

class PedidoGarcom(models.Model):
    garcom = models.ForeignKey(Garcom, on_delete=models.CASCADE)
    pratos = models.ManyToManyField(Prato)
    status = models.CharField(max_length=100)
    data_pedido = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Pedidos de Garçons'

    def __str__(self):
        return f"Pedido Garçom {self.id} - {self.garcom.nome}"

class OrdemProducao(models.Model):
    pedido = models.ForeignKey(PedidoCliente, on_delete=models.CASCADE)
    data_producao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Ordens de Produção'

    def __str__(self):
        return f"Ordem {self.id} - Pedido {self.pedido.id}"

class Entrega(models.Model):
    pedido = models.ForeignKey(PedidoCliente, on_delete=models.CASCADE)
    data_entrega = models.DateTimeField()
    status = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Entregas'

    def __str__(self):
        return f"Entrega {self.id} - Pedido {self.pedido.id}"

class Venda(models.Model):
    pedido = models.ForeignKey(PedidoCliente, on_delete=models.CASCADE)
    data_venda = models.DateTimeField(auto_now_add=True)
    tipo_venda = models.CharField(max_length=100)  # Ex.: "Entrega", "Retirada"

    class Meta:
        verbose_name_plural = 'Vendas'

    def __str__(self):
        return f"Venda {self.id} - Pedido {self.pedido.id}"

class ContatoCliente(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_contato = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField()

    class Meta:
        verbose_name_plural = 'Contatos com Clientes'

    def __str__(self):
        return f"Contato {self.id} - {self.cliente.nome}"

# Novo modelo Order
class Order(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    pratos = models.ManyToManyField(Prato)
    status = models.CharField(max_length=100, choices=[
        ('PENDENTE', 'Pendente'),
        ('EM_PROCESSO', 'Em Processo'),
        ('CONCLUIDO', 'Concluído'),
        ('CANCELADO', 'Cancelado'),
    ])
    data_pedido = models.DateTimeField(auto_now_add=True)
    data_entrega = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return f"Pedido {self.id} - {self.cliente.nome}"
