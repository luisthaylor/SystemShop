from Clientes import Cliente
from Clientes import Produto


class Sistema:
    def __init__(self):
        self.produtos = []
        self.clientes = []
        self.vendas = []  
        self.operacoes = []
        self.total_vendas = 0
        self.proximo_produto_id = 100
        self.proximo_cliente_id = 1

    def cadastrar_cliente(self):
        nome = input("Digite o nome do cliente: ")
        cliente = Cliente(self.proximo_cliente_id, nome)
        self.clientes.append(cliente)
        self.operacoes.append(("cadastro_cliente", cliente))
        print(f"Cliente cadastrado com sucesso! (ID gerado: {cliente.id})")
        self.proximo_cliente_id += 1

    def listar_clientes(self):
        if not self.clientes:
            print("Nenhum cliente cadastrado.")
        else:
            for c in self.clientes:
                print(f"ID: {c.id} | Nome: {c.nome} | Total gasto: R${c.total_gasto:.2f}")

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

    def realizar_venda(self):
        if not self.clientes:
            print("Nenhum cliente cadastrado.")
            return
        if not self.produtos:
            print("Nenhum produto no estoque.")
            return
        try:
            id_cliente = int(input("Digite o ID do cliente: "))
            cliente = next((c for c in self.clientes if c.id == id_cliente), None)
            if not cliente:
                print("Cliente não encontrado.")
                return
            id_produto = int(input("Digite o ID do produto: "))
            produto = next((p for p in self.produtos if p.id == id_produto), None)
            if not produto:
                print("Produto não encontrado.")
                return
            quantidade = int(input("Digite a quantidade: "))
        except ValueError:
            print("Entrada inválida.")
            return
        if quantidade > produto.quantidade:
            print("Quantidade indisponível.")
            return
        valor_total = quantidade * produto.preco
        produto.quantidade -= quantidade
        cliente.total_gasto += valor_total
        self.vendas.append((cliente, produto, quantidade, valor_total))
        self.total_vendas += valor_total
        self.operacoes.append(("venda", (cliente, produto, quantidade, valor_total)))
        print(f"Venda realizada com sucesso! (Valor total: R${valor_total:.2f})")

    def ver_fila_vendas(self):
        if not self.vendas:
            print("Nenhuma venda registrada.")
        else:
            for v in self.vendas:
                print(f"Cliente: {v[0].nome} | Produto: {v[1].nome} | Quantidade: {v[2]} | Valor: R${v[3]:.2f}")

    def desfazer_operacao(self):
        if not self.operacoes:
            print("Nenhuma operação para desfazer.")
            return
        tipo, dados = self.operacoes.pop()
        if tipo == "cadastro_produto":
            self.produtos.remove(dados)
            print(f"Cadastro do produto {dados.nome} desfeito.")
        elif tipo == "cadastro_cliente":
            self.clientes.remove(dados)
            print(f"Cadastro do cliente {dados.nome} desfeito.")
        elif tipo == "venda":
            cliente, produto, quantidade, valor = dados
            produto.quantidade += quantidade
            cliente.total_gasto -= valor
            self.total_vendas -= valor
            if (cliente, produto, quantidade, valor) in self.vendas:
                self.vendas.remove((cliente, produto, quantidade, valor))
            print("Venda desfeita com sucesso.")

    def valor_total_estoque(self):
        total = sum(p.quantidade * p.preco for p in self.produtos)
        print(f"Valor total do estoque: R${total:.2f}")

    def valor_total_vendas(self):
        print(f"Valor total de vendas realizadas: R${self.total_vendas:.2f}")

    def clientes_totais(self):
        if not self.clientes:
            print("Nenhum cliente cadastrado.")
        else:
            for c in self.clientes:
                print(f"Cliente: {c.nome} | Total gasto: R${c.total_gasto:.2f}")

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

    def salvar_estoque(self):
        try:
            with open("estoque.txt", "w", encoding="utf-8") as f:
                for p in self.produtos:
                    f.write(f"{p.id};{p.nome};{p.quantidade};{p.preco}\n")
            print("Estoque salvo em estoque.txt")
        except:
            print("Erro ao salvar estoque.")

    def carregar_estoque(self):
        try:
            with open("estoque.txt", "r", encoding="utf-8") as f:
                self.produtos.clear()
                for linha in f:
                    id, nome, qtd, preco = linha.strip().split(";")
                    produto = Produto(int(id), nome, int(qtd), float(preco))
                    self.produtos.append(produto)
            print("Estoque carregado com sucesso.")
        except FileNotFoundError:
            print("Arquivo estoque.txt não encontrado.")
        except:
            print("Erro ao carregar estoque.")