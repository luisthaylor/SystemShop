from Clientes import Cliente
from Clientes import Produto

import os
import json


class Sistema:
    def __init__(self):
        self.produtos = []
        self.clientes = []
        self.fila_vendas = []
        self.pilha_operacoes = []
        self.total_vendas = 0.0

        self.arquivo_produtos = "produtos.json"
        self.arquivo_clientes = "clientes.json"

        self.carregar_dados()

    def salvar_dados(self):
        with open(self.arquivo_produtos, "w", encoding="utf-8") as f:
            json.dump([p.__dict__ for p in self.produtos], f, indent=4, ensure_ascii=False)
        with open(self.arquivo_clientes, "w", encoding="utf-8") as f:
            json.dump([c.__dict__ for c in self.clientes], f, indent=4, ensure_ascii=False)

    def carregar_dados(self):
        if os.path.exists(self.arquivo_produtos):
            with open(self.arquivo_produtos, "r", encoding="utf-8") as f:
                lista = json.load(f)
                self.produtos = [Produto(**p) for p in lista]

        if os.path.exists(self.arquivo_clientes):
            with open(self.arquivo_clientes, "r", encoding="utf-8") as f:
                lista = json.load(f)
                self.clientes = [Cliente(**c) for c in lista]

    def gerar_id_produto(self):
        return len(self.produtos) + 1

    def gerar_id_cliente(self):
        return len(self.clientes) + 1

    def adicionar_produto(self, nome, quantidade, preco):
        novo = Produto(self.gerar_id_produto(), nome, quantidade, preco)
        self.produtos.append(novo)
        self.pilha_operacoes.append(("produto", novo))
        self.salvar_dados()
        print("✅ Produto adicionado com sucesso!")

    def listar_produtos(self):
        if not self.produtos:
            print("Nenhum produto cadastrado.")
        else:
            for p in self.produtos:
                print(p)

    def pesquisar_produto(self, termo):
        try:
            termo = int(termo)
            for p in self.produtos:
                if p.id == termo:
                    print(p)
                    return p
        except:
            for p in self.produtos:
                if termo.lower() in p.nome.lower():
                    print(p)
                    return p
        print("Produto não encontrado.")
        return None

    def adicionar_cliente(self, nome):
        novo = Cliente(self.gerar_id_cliente(), nome)
        self.clientes.append(novo)
        self.pilha_operacoes.append(("cliente", novo))
        self.salvar_dados()
        print("✅ Cliente adicionado com sucesso!")

    def listar_clientes(self):
        if not self.clientes:
            print("Nenhum cliente cadastrado.")
        else:
            for c in self.clientes:
                print(c)

    def realizar_venda(self, id_produto, id_cliente, quantidade):
        produto = next((p for p in self.produtos if p.id == id_produto), None)
        cliente = next((c for c in self.clientes if c.id == id_cliente), None)

        if not produto or not cliente:
            print("❌ Produto ou cliente inválido.")
            return

        if produto.quantidade < quantidade:
            print("❌ Estoque insuficiente.")
            return

        produto.quantidade -= quantidade
        valor = produto.preco * quantidade
        cliente.total_gasto += valor
        self.total_vendas += valor

        venda = {"produto": produto.nome, "cliente": cliente.nome, "quantidade": quantidade, "valor": valor}
        self.fila_vendas.append(venda)
        self.pilha_operacoes.append(("venda", venda))

        self.salvar_dados()
        print(f"✅ Venda realizada: {quantidade}x {produto.nome} para {cliente.nome} - R${valor:.2f}")

    def visualizar_vendas(self):
        if not self.fila_vendas:
            print("Nenhuma venda registrada.")
        else:
            for v in self.fila_vendas:
                print(f"{v['cliente']} comprou {v['quantidade']}x {v['produto']} - R${v['valor']:.2f}")

    def desfazer_operacao(self):
        if not self.pilha_operacoes:
            print("Nenhuma operação para desfazer.")
            return

        tipo, obj = self.pilha_operacoes.pop()
        if tipo == "produto":
            self.produtos.remove(obj)
            print("❌ Último produto removido (desfeito).")
        elif tipo == "cliente":
            self.clientes.remove(obj)
            print("❌ Último cliente removido (desfeito).")
        elif tipo == "venda":
            for p in self.produtos:
                if p.nome == obj["produto"]:
                    p.quantidade += obj["quantidade"]
            for c in self.clientes:
                if c.nome == obj["cliente"]:
                    c.total_gasto -= obj["valor"]
            self.total_vendas -= obj["valor"]
            self.fila_vendas.pop()
            print("❌ Última venda desfeita.")
        self.salvar_dados()

    def exibir_valor_estoque(self):
        total = sum(p.preco * p.quantidade for p in self.produtos)
        print(f"💰 Valor total do estoque: R${total:.2f}")

    def exibir_total_vendas(self):
        print(f"💵 Valor total de vendas realizadas: R${self.total_vendas:.2f}")

    def exibir_clientes_valores(self):
        for c in self.clientes:
            print(f"{c.nome} - Total gasto: R${c.total_gasto:.2f}")
