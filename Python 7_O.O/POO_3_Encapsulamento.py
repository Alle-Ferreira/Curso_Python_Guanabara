'''
Conceitos de POO:

1. Encapsulamento: 

Protege os dados de uma classe, tornando-os acessíveis apenas através de métodos.
   - Atributos privados são precedidos por um underscore (_).
   - Métodos públicos são acessíveis fora da classe, enquanto métodos privados não são.
   - Permite controlar o acesso aos dados e garantir a integridade do objeto.

Vantagens do Encapsulamento
    - Tornar mudanças invisíveis
    - Facilitar a reutilização do código
    - Reduzir efeitos colaterais
'''

class Conta:

    def __init__(self, nro_agencia, saldo = 0):
        self.nroagencia = nro_agencia
        self._saldo = saldo   # "_" antes da palavra saldo define o recurso como privado.

    # As alterações envolvendo "_saldo" devem ser executadas dentro das funções da classe Conta, pois é recurso privado.
    # O sistema não bloqueará a alteração fora das funções, mas a convenção deve ser respeitada.
    
    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo += valor

    def mostrar_saldo(self):
        return self._saldo


conta1 = Conta("0001", 100)         # Criando a instancia
conta1.depositar(100)               # Usando método da classe

conta2 = Conta(100)                 # Criando a instancia
conta2._saldo += 100                # Alterando diretamente: desrespeita a convenção privada para o "_saldo"

print(conta1.nroagencia)
print(conta2.mostrar_saldo)
print()


'''
1.1. Propriedades

Decorador é como uma função, executada antes da função da Classe.

a) @property: permite acessar o resultado do método como uma variável.

b) @setter: valor a ser atribuido à variavel.

c) @deleter
'''
class Aluno:
    def __init__(self, exemplo = None):
        self._exemplo = exemplo
    
    @property      
    def exemplo(self):
        return self._exemplo or 0
    
    @exemplo.setter
    def exemplo(self, valor):
        _exemplo = self._exemplo or 0
        _valor = valor or 0
        self._exemplo = _exemplo + _valor
    
    @exemplo.deleter
    def exemplo(self):
        self._exemplo = -1

aluno1 = Aluno(10)        
print(aluno1.exemplo)

aluno1.exemplo = 10       # valor a ser atribuido à variavel exemplo.
print(aluno1.exemplo)

del aluno1.exemplo
print(aluno1.exemplo)
print()
