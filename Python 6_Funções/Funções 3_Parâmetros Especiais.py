'''
Subprogramas: Parâmetros Especiais

I - Argumentos

Por padrão, argumentos podem ser passados:

- por nome (keyword only): depois do '*' somente por palavra-chave.
- por posição (positional only): antes da '/' somente por posição.
- por posição e nome

Estrutura da Sintaxe:

def f(position1, position2, /, position_or_keyword, *, keyword1, keyword2):


1. Exemplo Positional Only:'''

def criar_carro(modelo, ano, placa, /, marca, motor, combustível):
    print(modelo, ano, placa, marca, motor, combustível)


criar_carro('Palio', 1999, 'abc-1234', marca='fiat', motor='1.0', combustível='gasolina')       # válida

''' 
criar_carro(modelo='Palio', ano=1999, placa='abc-1234', marca='fiat', motor='1.0', combustível='gasolina')
#Invalida: (os parametros antes da barra "/" (modelo, ano, placa) deveriam ser por posição, e não por palavra-chave)


2. Exemplo Keyword Only (*)'''

def criar_carro(*, modelo, ano, placa, marca, motor, combustível):
    print(modelo, ano, placa, marca, motor, combustível)


criar_carro(modelo='Palio', ano=1999, placa='abc-1234', marca='fiat', motor='1.0', combustível='gasolina')        # válida

''' 
criar_carro('Palio', 1999, 'abc-1234', marca='fiat', motor='1.0', combustível='gasolina')
#Invalida: (ao colocar o '*' no inicio da declaração da função, obrigou todos os argumentos a serem por chave-valor)


3. Exemplo Híbrido: Positional and Keyword'''

def criar_carro(modelo, ano, placa, /, marca, *, motor, combustível):
    """ antes da barra: por posição
        depois do asterisco: por palavra-chave
        entre os dois: pode ser um ou outro."""
    print(modelo, ano, placa, marca, motor, combustível)


criar_carro('Palio', 1999, 'abc-1234', marca='fiat', motor='1.0', combustível='gasolina')   # válida
#antes da barra (modelo, ano, placa): por posição
#depois do asterisco (motor, combustível): por palavra-chave
#entre os dois (marca): pode ser um ou outro.