'''
Métodos em POO

1 - Métodos Construtores e Destrutores

a) Método Construtor: __init__
    - É chamado automaticamente quando um objeto é criado.
    - Inicializa os atributos do objeto.
    - Pode receber parâmetros para definir o estado inicial do objeto.
      Exemplo: __init__(self, atributo1, atributo2)

b) Método Destrutor: __del__
    - É chamado automaticamente quando um objeto é destruído ou removido da memória.
    - É usado para liberar recursos ou realizar ações de limpeza.
      Exemplo: __del__(self)
'''

class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def __del__(self):
        print(f'O carro {self.modelo} foi removido.')  


'''
2 - Métodos de Classe: cls - @classmethod

- Recebe um primeiro argumento que aponta para a classe
- Pode acessar ou modificar o estado da classe.
- Estão ligados à classe e não à estancia do objeto.
- Usado para criar métodos de fábrica (retorna instancias da classe)

Por convenção chama 'cls'
'''
class Pessoa:

    def __init__(self, nome = None, idade = None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_por_dt_nascimento(cls, dia, mes, ano, nome):
        idade = 2025 - ano
        return cls(nome, idade)

p1 = Pessoa.criar_por_dt_nascimento(7, 12, 1988, 'Ally')
print(p1.nome, p1.idade)
print()

'''
3 - Métodos Estáticos: @staticmethod

- Não recebem um primeiro argumento explicito
- Não pode acessar ou modificar o estado da classe.
- Também estão ligados à classe e não à estancia do objeto.
- Usado para criar funções utilitárias, como funções de validação.
'''

class Pessoas:

    def __init__(self, nome = None, idade = None):
        self.nome = nome
        self.idade = idade
    
    @staticmethod
    def maioridade(idade):     #retorno booleano: True /False
        return idade >= 18
    
print(Pessoas.maioridade(18))  
print(Pessoas.maioridade(8))


'''
4 - Métodos Getter e Setter

Get
Set
'''