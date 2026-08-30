from produto import *
import time
class CarrinhoDeCompras:
    def __init__(self):
        self.__itens = []

    def adiciona_item(self, nome: str,):
        for produto in produtos:
            if produto.nome == nome:
                self.__itens.append(produto)
                return 

    def remove_item(self, nome: str):
        for produto in self.__itens:
            if produto.nome == nome:
                print(produto)
                self.__itens.remove(produto)

    @property              
    def total(self):
        total = 0.0
        for item in self.__itens: 
            total += item.preco     
        return  f'O valor Total do caarinho e R$: {total}'  
                  
    def __repr__(self):
        formato = 'CarrinhoDeCompras('
        for item in self.__itens:
            formato += str(item)
        formato += '\n)'
        return formato

    def __str__(self):
        formato = '🛒 (Carrinho de compras)\n'
        formato += '-' * 23 + '\n'
        if self.__itens == []:
            formato += 'Vazio... \n'
            formato += '-' * 23 + '\n'
        else:
            for item in self.__itens:
                formato += f'Nome.......: {item.nome}\n'
                formato += f'Preço......: R$ {item.preco:.2f}\n'
                formato += f'Categoria..: {item._categoria}\n'
                formato += '-' * 23 + '\n'
            formato += f'{self.total}\n'
            formato += '-' * 23 + '\n'
        return formato

def main():
    produtos.append(Produto('iPhone 17', 5000.00, 'Roupas'))
    produtos.append(Produto('MackBook', 5000.00, 'Eletronico'))
    c1 = CarrinhoDeCompras()
    #p1 = Produto('iPhone 17', 5000.00, 'Roupas')
    #p2 = Produto('Fone de ouvido', 200.00, 1)
    #p3 = Produto('MacBook', 8000.00, 3)
    print(c1)
    #print()
    c1.adiciona_item('iPhone 17')
    c1.adiciona_item('MackBook')
    time.sleep(3)
    print(c1)
    c1.remove_item('MackBook')
    time.sleep(3)
    print(c1)


if __name__ == '__main__':
    main()