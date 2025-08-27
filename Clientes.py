import os
import time


class Produto:
    def __init__(self, id_produto, nome, quantidade, preco):
        self.id = id_produto
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def __str__(self):
        return f"[{self.id}] {self.nome} - {self.quantidade} un - R${self.preco:.2f}"

class Cliente:
    def __init__(self, id_cliente, nome):
        self.id = id_cliente
        self.nome = nome
        self.total_gasto = 0.0

    def __str__(self):
        return f"[{self.id}] {self.nome} - Total gasto: R${self.total_gasto:.2f}"
