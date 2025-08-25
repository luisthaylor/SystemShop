from Clientes import Cliente
from Clientes import Produto


def carregar_estoque(self):
    try:
        with open("estoque.txt", "r") as file:
            self.produtos.clear()
            self.clientes.clear()
            for line in file:
                if line.strip():
                    parts = line.strip().split(",")
                    if parts[0] == "PRODUTO" and len(parts) == 4:
                        _, nome, quantidade, preco = parts
                        produto = Produto(nome, int(quantidade), float(preco))
                        self.produtos.append(produto)
                    elif parts[0] == "CLIENTE" and len(parts) == 3:
                        _, nome, total_gasto = parts
                        cliente = Cliente(nome)
                        cliente.total_gasto = float(total_gasto)
                        self.clientes.append(cliente)
                    elif parts[0] == "TOTAL_ESTOQUE" and len(parts) == 2:
                        self.total_estoque = float(parts[1])
                    elif parts[0] == "TOTAL_VENDAS" and len(parts) == 2:
                        self.total_vendas = float(parts[1])
        print("Estoque carregado com sucesso!")
    except FileNotFoundError:
        print("Arquivo de estoque não encontrado. Um novo será criado.")
    except Exception as e:
        print(f"Erro ao carregar estoque: {e}")
