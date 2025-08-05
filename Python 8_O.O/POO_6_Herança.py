'''
Conceitos de POO:

3. Herança: 

Permite criar uma nova classe baseada em uma classe existente.
   - A nova classe herda atributos e métodos da classe base.
   - Pode adicionar novos atributos e métodos ou modificar os existentes.'''

class Veiculo:
    def __init__(self, tipo, qtde_rodas):
        self.tipo = tipo
        self.qtde_rodas = qtde_rodas

    def __str__(self):      
        return f'{self.__class__.__name__}: {', '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}'

veiculo_1 = Veiculo('Carro', 4)
veiculo_2 = Veiculo('Moto', 2)
veiculo_3 = Veiculo('Caminhao', 6)

class Caminhao(Veiculo):
    def __init__(self, modelo, ano, cor, tipo, qtde_rodas):
        super().__init__(tipo, qtde_rodas)
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

caminhao_1 = Caminhao('Volvo FH', 2020, 'Branco', tipo=veiculo_3.tipo, qtde_rodas=veiculo_3.qtde_rodas)
print(caminhao_1) 
print()

