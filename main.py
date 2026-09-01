from produto import *
from carrinho_compras import *
from cliente import *
import time
clientes = []

def menu_produto():                  
        opcao_produto = int(input("""
╔════════════════════════════════╗
║       MENU DE PRODUTOS         ║
╠════════════════════════════════╣
║  1 - Novo produto              ║
║  2 - Excluir produto           ║
║  3 - Ver produtos              ║
║  4 - Voltar                    ║
║  0 - Sair do programa          ║
╚════════════════════════════════╝
Escolha uma opção: """))
        match opcao_produto:

            case 1:
                resposta = 'S'
                while resposta == 'S':
                    CriarProduto()
                    resposta = input("Deseja Cadastrar um novo Produto? (S/N)\n").lower()
                menu_produto()    

            case 2:
                for produto in produtos:
                    print(produto)
                resposta = 'S'    
                while resposta == 'S':     
                    n = input("Escolha o nome do  produto que deseja remover!!! \n").lower()  
                    RemoverProduto(n)
                    resposta = input("Deseja remover um produto? (S/N) \n").lower()
                else: 
                    menu_produto()
           
            case 3:
                for produto in produtos:
                    print(produto)
                resposta = int(input("Digite 0 para voltar ao menu!!! \n"))
                if resposta == 0:
                    menu_produto()
                else: 
                    print()     

            case 4:
                time.sleep(1)
                menu_inicial()
                                                                    
            case 0:
                print("Saindo do programa...")
                time.sleep(1)
                exit()

def menu_cliente():
    opcao_cliente = int(input("""
╔════════════════════════════════╗
║        MENU DE USUÁRIO         ║
╠════════════════════════════════╣
║  1 - Novo cliente              ║
║  2 - Ver clientes              ║
║  3 - Adicionar cupom           ║
║  4 - Voltar                    ║
║  0 - Sair do programa          ║
╚════════════════════════════════╝
Escolha uma opção: """))

    match opcao_cliente:

        case 1:
            try:
                nome = input("Digite o nome do cliente: ")
                email = input("Digite o e-mail do cliente: ")
                cpf = input("Digite o CPF (999.999.999-99): ")

                cliente = Cliente(nome, email, cpf)

                clientes.append(cliente)

                print("\nCliente cadastrado com sucesso!!!")

            except ValueError as erro:
                print(f"\nErro ao cadastrar cliente: {erro}")

            input("\nPressione ENTER para continuar...")
            menu_cliente()

        case 2:
            if not clientes:
                print("Nenhum cliente cadastrado.")
            else:
                for cliente in clientes:
                    print(cliente)
                    print(
                        f"Saldo em cupons: "
                        f"R$ {cliente.saldo_cupom}"
                    )

            input("\nPressione ENTER para continuar...")
            menu_cliente()

        case 3:
            if not clientes:
                print("\nNenhum cliente cadastrado.")
                menu_cliente()
                return

            for indice, cliente in enumerate(clientes, start=1):
                print(f"{indice} - {cliente.nome}")

            try:
                escolha = int(input("Escolha o cliente: "))

                if escolha < 1 or escolha > len(clientes):
                    print("Cliente inválido.")
                    menu_cliente()
                    return

                cliente = clientes[escolha - 1]

                valor = float(
                    input("Digite o valor do cupom: R$ ").replace(",", ".")
                )

                cliente.saldo_cupom = valor

                print("\nCupom adicionado com sucesso!!!")
                print(
                    f"Saldo atual de cupons: "
                    f"R$ {cliente.saldo_cupom}"
                )

            except ValueError as erro:
                print(f"\nErro: {erro}")
                
            input("\nPressione ENTER para continuar...")
            menu_cliente()

        case 4:
            menu_inicial()

        case 0:
            print("Saindo do programa...")
            exit()

def menu_carrinho(c1):
        opcao_carrinho = int(input("""
╔════════════════════════════════╗
║        MENU DO CARRINHO        ║
╠════════════════════════════════╣
║  1 - Adicionar item            ║
║  2 - Remover item              ║
║  3 - Ver carrinho              ║
║  4 - Voltar                    ║
║  0 - Sair do programa          ║
╚════════════════════════════════╝
Escolha uma opção: """))

        match opcao_carrinho:

            case 1:
                resposta = 'S'
                while resposta == 'S':
                    for produto in produtos:
                        print(produto)
                    n = input("Digite o nome do produto que voce deseja adicionar ao carrinho!!!\n") 
                    c1.adiciona_item(n)
                    print(c1)
                    print("O produto selecionado foi adicionado ao carrinho com sucesso!!!")
                    resposta = input("Deseja adicionar um  item no seu carrinho? (S/N) \n")
                else:
                    menu_carrinho(c1)                                           
            case 2:
                resposta = 'S'
                while resposta == 'S':
                    for item in c1._CarrinhoDeCompras__itens:
                        print(item)
                    n = input("Digite o nome do produto que deseja remover.\n")
                    p = c1.remove_item(n)
                    print(f'{c1}\n O produto selecionado foi removido do carrinho com sucesso!!!')
                    resposta = input("Deseja remover um item do seu carrinho? (S/N) \n")
                else:
                    menu_carrinho(c1)    
            case 3:
                print(c1)
                c1.utilizar_cupom()
                print(c1)
                resposta = int(input("Digite 0 para voltar ao menu!!! \n"))
                if resposta == 0:
        	        menu_carrinho(c1)
            case 4:
                menu_inicial()

            case 0:  
                print("Saindo do programa...")
                exit() 

def menu_inicial():
        opcao = int(input("""
╔════════════════════════════════╗
║           MENU LOJA            ║
╠════════════════════════════════╣
║  1 - Produto                   ║
║  2 - Cliente                   ║
║  3 - Carrinho                  ║
║  0 - Sair                      ║
╚════════════════════════════════╝
Escolha uma opção: """))
        match opcao: 

            case 1:
                menu_produto()

            case 2:
                menu_cliente()

            case 3:
                while True:
                    for cliente in clientes:
                        print(cliente)
                    clte = input("Escolha um Clinte para continuar!! \n")
                    cliente_encontrado = False
                    for cliente in clientes:
                        if clte == cliente.nome:  
                            c1 = CarrinhoDeCompras(clte, clientes)
                            print("Cliente Selecionado com sucesso!!")
                            cliente_encontrado = True
                            break
                    if cliente_encontrado:
                        break    
                    else:
                        print("Cliente não cadastrado!!! ")              
                menu_carrinho(c1)

            case 0:
                resposta = input("Tem certeza que deseja encerrar? (S/N) \n")
                while resposta == 'S':
                    break

                     
menu_inicial()        