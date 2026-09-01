import time
produtos =[]

def CriarProduto():
    nome = input("Digite aqui o nome do seu produto: \n")
    preco = float(input("Digite aqui o valor do seu produto: \n"))
    categoria = input("digite aqui a categoria do seu produto: \n")

    try:
        produto = Produto(nome, preco, categoria)
        produtos.append(produto)
        time.sleep(1)
        print(f'{produto}\n')
        print("Produto criado!!!")
        
    except ValueError as erro:
        print(f" Erro: {erro}")

def RemoverProduto(nome: str):
    for produto in produtos:
        if nome == produto.nome:
            print(f"O Produto : {produto.nome} foi removido com sucesso!")
            produtos.remove(produto)
        else:
            print("Produto não encontrado")

class Produto:
    def __init__(self, nome: str, preco: float, categoria: str):
        self.nome = nome                # Atributo público
        self._categoria = categoria     # Atributo com resalvas 
        self.preco = preco              # Atributo "protegido"

    def __repr__(self):
        formato = f'Produto(nome={self.nome}, ' + \
                  f'categoria={self._categoria}, ' + \
                  f'preco={self.preco})'
        return formato

    def __str__(self):
        formato = f'🎁\n' + \
                  f'Nome......: {self.nome}\n' + \
                  f'Categoria ....: {self._categoria}\n' +\
                  f'Preço.....: R$ {self.preco:.2f}\n'                
        return formato

    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, valor):
        if valor > 0:
            self.__preco = valor
        else:
            raise ValueError ('Preço não pode ser negativo')    

if __name__ == '__main__':
    main
