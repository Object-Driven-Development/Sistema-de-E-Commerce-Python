from produto import *
from carrinho_compras import *
import time
c1 = CarrinhoDeCompras()

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
                    resposta = input("Deseja Cadastrar um novo Produto? (S/N)")
                menu_produto()    

            case 2:
                for produto in produtos:
                    print(produto)
                resposta = 'S'    
                while resposta == 'S':     
                    n = input("Escolha o nome do  produto que deseja remover!!! \n")  
                    RemoverProduto(n)
                    resposta = input("Deseja remover um produto? (S/N) \n")
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
                exit()

def menu_carrinho():
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
                    menu_carrinho()                              
            case 2:
                resposta = 'S'
                while resposta == 'S':
                    for produto in produtos:
                        print(produto)
                    n = input("Digite o nome do produto que deseja remover.\n")
                    p = c1.remove_item(n)
                    print(f'{p}\n O produto selecionado foi removido do carrinho com sucesso!!!')
                    resposta = input("Deseja remover um item do seu carrinho? (S/N) \n")
            case 3:
                print(c1)

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
║  2 - Usuário                   ║
║  3 - Carrinho                  ║
║  0 - Sair                      ║
╚════════════════════════════════╝
Escolha uma opção: """))
        match opcao: 

            case 1:
                menu_produto()

            case 2:
                menu_carrinho()

            case 3:
                menu_carrinho()

            case 0:
                resposta = input("Tem certeza que deseja encerrar? (S/N) \n")
                while resposta == 'S':
                    break

                     
menu_inicial()        