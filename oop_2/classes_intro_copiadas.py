#Definir as variaveis dentro da classe para depois criar o objeto
#por isso usamos o self

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
       
#Define a saudação
    def saudacao(self):
        return f"O meu nome é {self.nome} e tenho {self.idade} anos."
 
#Mesma coisa da linha 1 e 2 (Class pessoa)
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

#Informações do objeto
    def informacao_do_carro(self):
        return f"Este é um {self.marca} {self.modelo}."