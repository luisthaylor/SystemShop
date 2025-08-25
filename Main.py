from SistemaVendas import Sistema
from Clientes import Cliente
from Clientes import Produto


def main():
    sistema = Sistema()
    while True:
        print("===== MENU ESTOQUE =====")
        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("3 - Cadastrar produto")
        print("4 - Listar produtos")
        print("5 - Realizar venda")
        print("6 - Ver fila de vendas")
        print("7 - Desfazer última operação")
        print("8 - Exibir valor total do estoque")
        print("9 - Exibir valor total de vendas realizadas")
        print("10 - Exibir clientes e valores totais gastos")
        print("11 - Pesquisar produto")
        print("12 - Salvar estoque em arquivo")
        print("13 - Carregar estoque de arquivo")
        print("14 - Sair")
        opcao = input("Escolha: ")
        if opcao == "1":
            sistema.cadastrar_cliente()
        elif opcao == "2":
            sistema.listar_clientes()
        elif opcao == "3":
            sistema.cadastrar_produto()
        elif opcao == "4":
            sistema.listar_produtos()
        elif opcao == "5":
            sistema.realizar_venda()
        elif opcao == "6":
            sistema.ver_fila_vendas()
        elif opcao == "7":
            sistema.desfazer_operacao()
        elif opcao == "8":
            sistema.valor_total_estoque()
        elif opcao == "9":
            sistema.valor_total_vendas()
        elif opcao == "10":
            sistema.clientes_totais()
        elif opcao == "11":
            sistema.pesquisar_produto()
        elif opcao == "12":
            sistema.salvar_estoque()
        elif opcao == "13":
            sistema.carregar_estoque()
        elif opcao == "14":
            print("Saindo do sistema... Até logo!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
