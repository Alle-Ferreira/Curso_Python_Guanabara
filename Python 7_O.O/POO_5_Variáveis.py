'''
Conceitos de POO: Interfaces e Classes Abstratas

4. Variáveis de Classe e de Instancia

Objetos nascem com o mesmo numero de atributos de classe e de instancia.

- Atributos de instancia sao diferentes para cada objeto.
- Atributos de classe são compatilhados entre os objetos.
'''

class Estudante:
    escola = 'Dio'

    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero

    def __str__(self):
        return f'{self.__class__.__name__}: {", ".join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}'

def __str__(self):
    return f'{self.nome} - {self.numero} - {self.escola}'

def mostrar_valores(*objetos):           # espera uma coleção de objetos iteráveis.
    for objeto in objetos:
        print(objeto)


Estudante_1 = Estudante('Guilherme', 56451)
Estudante_2 = Estudante('Giovanna', 17323)

print(1)
print(Estudante_1)
print(Estudante_2)

print(2)
mostrar_valores(Estudante_1, Estudante_2)

