import os
import time


class Produto:
    def __init__(self, id, nome, quantidade, preco):
        self.id = id
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

class Cliente:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        self.total_gasto = 0

