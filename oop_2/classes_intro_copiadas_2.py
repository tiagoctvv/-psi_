#import para o ficheiro as bluesprints
from classes_intro_blueprints import Pessoa
from classes_intro_blueprints import Carro
 
#Criação do objeto
pessoa = Pessoa("Tiago", 16)
carro = Carro("lamborguini", "Ignus")
 
#Mostra os objetos
print(pessoa.saudacao())
print(carro.informacao_do_carro())