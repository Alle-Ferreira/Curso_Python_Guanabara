'''
1 - Interfaces
Interfaces são conjuntos de métodos abstratos de uma classe.

- O conceito de interface é definido com um Contrato.
- Define o que uma classe deve ou não fazer, mas não especifica "como' fazer.
- Declara os métodos e as respectivas assinaturas
- O método é previsto, mas nao implementado.
- Os métodos abstratos de uma interface via de regra sao publicos.


2. Classes Abstratas
A interface é a mesma, mas a implementação é diferente. 

- Os atributos sao todos privados.
- Em python utilizamos classes abstratas para criar contratos.
- Classes abstratas não podem ser instanciadas.
- Herdeiros serão obrigados a implementar todos os métodos abstratos da classe pai.

a) Criando Classes Abstratas com módulo ABC
Por padrão, o Python não fornece classes abstratas. Mas vem com o módulo ABC.

b) Módulo ABC (Abstract Base Class)
- Decora métodos da classe base como abstratos: @abstractmethod
- Registra classes concretas como implementações da base abstrata.
'''

from abc import ABC, abstractmethod

class Controles(ABC):
    
    @abstractmethod
    def ligar(self):                # estabelecendo Contrato
        pass

    @abstractmethod                 # estabelecendo Contrato
    def desligar(self):
        pass

    @property
    @abstractmethod                 # estabelecendo Contrato (@abstractproperty obsoleto)
    def distancia(self):
        pass

class Controle_TV(Controles):

    def ligar(self):                # Implementação Obrigatória
        print('Ligando TV')

    def desligar(self):             # Implementação Obrigatória
        print('Desligando TV')
    
    @property
    def distancia(self):
        return '6 mts'

class Controle_Som(Controles):

    def ligar(self):                # Implementação Obrigatória
        print('Ligando som')

    def desligar(self):             # Implementação Obrigatória
        print('Desligando som')
    
    @property
    def distancia(self):
        return '4.5 mts'


ale_tv = Controle_TV()

ale_tv.ligar()
ale_tv.desligar()
print(ale_tv.distancia)


ale_som = Controle_Som()

ale_som.ligar()
ale_som.desligar()
print(ale_som.distancia)