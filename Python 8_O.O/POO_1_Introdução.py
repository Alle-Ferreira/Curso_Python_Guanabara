''' Objetos de Primeira Classe

Em Python tudo é objeto.
Funções são objetos de primeira classe.
Strings são objetos de primeira classe.

Objetos de primeira classe podem ser:
- atribuidos a variaveis
- passados como parametros
- usados como estrutura de dados (listas, tulipas, dicionarios)
- usados como valor de retorno (closures)

1. Classes são objetos de primeira classe.

Uma classe define as características e comportamentos de um objeto.
'''

class Cachorro:
    def __init__(self, nome, cor, acordado = True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def latir(self):
        print('Au Au Au!')
        print(f'{self.nome} está latindo!')

    def dormir(self):
        self.acordado = False
        print('Zzz... Zzz...')
        print(f'{self.nome} está dormindo!')

'''
2. Objetos são instâncias de classes.

Objetos são instâncias de classes, ou seja, são criados a partir de uma classe.
Objetos possuem atributos e métodos que definem seu estado e comportamento, definidos na classe.
'''

cao_1 = Cachorro('Chapie', 'Marrom', False)
cao_2 = Cachorro('Aladim', 'Branco e Preto')


'''3. Exemplos de Uso

a). Nos métodos da classe Cachorro:'''

cao_1.latir()

print(cao_2.acordado)                   # Verifica se o cao_2 está acordado: responde com True ou False
cao_2.dormir()                          # Faz o cao_2 dormir, alterando o atributo acordado para False  
print(cao_2.acordado)
print()

'''
b). Criando a classe Bicicleta:'''

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, nro_marcha=1):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.nro_marcha = nro_marcha
    
    def buzinar(self):
        print('Plim plim...')

    def parar(self):
        print('Parando a bicicleta...')
        print(f'Bicicleta {self.modelo} parada!')

    def correr(self):
        print('Vrum vrum...')

    def trocar_marcha(self):
        if self.nro_marcha > 1:
            print(f'Quantidade de marchas da bicicleta: {self.nro_marcha}. Marcha trocada!')
        else:
            print('Não foi possível trocar a marcha!')

    def __str__(self):      # Método para exibir a representação da classe.
        return f'{self.__class__.__name__}: {', '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}'
'''
    def __str__(self):     # Representação da classe Bicicleta: manutenção mais detalhada.
        return f'Bicicleta {self.modelo} - Cor: {self.cor} - Ano: {self.ano} - Valor: R$ {self.valor:.2f}
'''


bike_1 = Bicicleta('Vermelha', 'Caloi', 2022, 600.00)
bike_2 = Bicicleta('Preta', 'Monark', 2023, 800.00, 3)

bike_1.buzinar()
bike_2.correr()
bike_1.parar()
print(f'Bike 1: modelo {bike_1.modelo}, cor {bike_1.cor}, valor {bike_1.valor}')
bike_2.trocar_marcha()  
print()

print(bike_1)   # Exibe representação STR da bicicleta bike_1
print(bike_2)   # Exibe representação STR da bicicleta bike_2
print()

