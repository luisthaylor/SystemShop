import os
import time

class Produto:
    def __init__(self, id, nome, quantidade, preco):
        self.id = id
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def cadastrar_produto(self):
        nome = input("Digite o nome do produto: ")
        try:
            quantidade = int(input("Digite a quantidade: "))
            preco = float(input("Digite o preço: "))
        except ValueError:
            print("Entrada inválida.")
            return
        produto = Produto(self.proximo_produto_id, nome, quantidade, preco)
        self.produtos.append(produto)
        self.operacoes.append(("cadastro_produto", produto))
        print(f"Produto cadastrado com sucesso! (ID gerado: {produto.id})")
        self.proximo_produto_id += 1

    def listar_produtos(self):
        if not self.produtos:
            print("Estoque vazio.")
        else:
            for p in self.produtos:
                print(f"ID: {p.id} | Nome: {p.nome} | Quantidade: {p.quantidade} | Preço: R${p.preco:.2f}")

    def pesquisar_produto(self):
        if not self.produtos:
            print("Nenhum produto no estoque.")
            return
        escolha = input("Pesquisar por (1) ID ou (2) Nome: ")
        if escolha == "1":
            try:
                id_busca = int(input("Digite o ID do produto: "))
            except ValueError:
                print("ID inválido.")
                return
            produto = next((p for p in self.produtos if p.id == id_busca), None)
            if produto:
                print(f"ID: {produto.id} | Nome: {produto.nome} | Quantidade: {produto.quantidade} | Preço: R${produto.preco:.2f}")
            else:
                print("Produto não encontrado.")
        elif escolha == "2":
            nome_busca = input("Digite o nome do produto: ").lower()
            encontrados = [p for p in self.produtos if nome_busca in p.nome.lower()]
            if encontrados:
                for p in encontrados:
                    print(f"ID: {p.id} | Nome: {p.nome} | Quantidade: {p.quantidade} | Preço: R${p.preco:.2f}")
            else:
                print("Nenhum produto encontrado.")
        else:
            print("Opção inválida.")
