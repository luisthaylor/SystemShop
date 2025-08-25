from Clientes import Cliente
from Clientes import Produto



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