from SistemaVendas import Sistema
from Clientes import Cliente
from Clientes import Produto

from SistemaVendas import Sistema

def main():
    sistema = Sistema()

    while True:
        print("\n===== MENU ESTOQUE =====")
        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("3 - Cadastrar produto")
        print("4 - Listar produtos")
        print("5 - Realizar venda")
        print("6 - Visualizar fila de vendas")
        print("7 - Desfazer última operação")
        print("8 - Exibir valor total do estoque")
        print("9 - Exibir valor total de vendas realizadas")
        print("10 - Exibir clientes e valores totais gastos")
        print("11 - Pesquisar produto por nome ou ID")
        print("0 - Sair")
        print("========================")

        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Nome do cliente: ")
            sistema.adicionar_cliente(nome)

        elif opcao == "2":
            sistema.listar_clientes()

        elif opcao == "3":
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade: "))
            preco = float(input("Preço: "))
            sistema.adicionar_produto(nome, quantidade, preco)

        elif opcao == "4":
            sistema.listar_produtos()

        elif opcao == "5":
            id_produto = int(input("ID do produto: "))
            id_cliente = int(input("ID do cliente: "))
            quantidade = int(input("Quantidade: "))
            sistema.realizar_venda(id_produto, id_cliente, quantidade)

        elif opcao == "6":
            sistema.visualizar_vendas()

        elif opcao == "7":
            sistema.desfazer_operacao()

        elif opcao == "8":
            sistema.exibir_valor_estoque()

        elif opcao == "9":
            sistema.exibir_total_vendas()

        elif opcao == "10":
            sistema.exibir_clientes_valores()

        elif opcao == "11":
            pesquisa = input("Digite nome ou ID do produto: ")
            sistema.pesquisar_produto(pesquisa)

        elif opcao == "0":
            print("Saindo do sistema... Até logo!")
            break

        else:
            print("⚠ Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
