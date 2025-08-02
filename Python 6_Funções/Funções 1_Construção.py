'''
Subprogramas: Procedimentos e Funções

Os subprogramas podem ser procedimentos e funções.
- Procedimentos: são aqueles que não retornam valores.
- Funções: são aquelas que retornam valores.

Na maioria das linguagens que não explicita a diferença entre ambos, as funções podem ser definidas sem retornar qualquer valor, tendo um comportamento de procedimento. Esse é o caso de Python.

I - Funções

Bloco de código identificado por um nome. Programar por Funções é programar estruturado.
Pode receber uma lista de parametros, com ou sem parametros padronizados.
Por padrão, toda função, sem um valor declarado explicito, retorna NONE.

II - Variaveis

a) Variáveis locais: são definidas pelo sub-programa, as quais tem seu escopo usualmente é o corpo do subprograma.
   - Normalmente podem ser dinamicas da pilha ou estáticas.
   - Mas no Python, todas as variáveis locais são dinâmicas da pilha.

b) Variáveis Globais: são declaradas em definições de método: portanto, precisam ser definida fora dele. 
   Caso haja uma variável local com o mesmo nome de uma variável global:
    - A global é implicitamente declarada como local dentro da função.
    - Para alterar a variável global, seria necessário explicitar, dentro de cada função, que o nome da variável é referente a ela. 
    - Isso pode ser feito com a palavra reservada 'global'.

    
1. Etapas da Contrução das Funções:

a) Declarando as funções: DEF'''

def diga_oi():                                        #Função sem argumentos
    print('Hello, World!')
    
def exibir_msg_2(nome):                               #Função com 01 argumento
    print(f'Very Welcome {nome}!')

def exibir_msg_3(nome = "Anônimo"):                   # Função com 01 argumento opcional: o padrão definido "Anonimo" é usado caso não receba o parametro.
    print(f'Very Welcome {nome}!')                    

def somar_numeros(a=0, b=0, c=0):                     # Função com todos os parametros opcionais.                      
    soma = sum(a, b, c)
    print(soma)


'''
b) Chamando as funções procedimentais (sem retorno de parametros), dentro do programa principal:'''

diga_oi()

exibir_msg_2(nome = 'Alessandra')

exibir_msg_3()                      #sem passar o parametro NOME, ele usará o q está definido por padrão ("Anonimo").
exibir_msg_3(nome = "Alessandra")   #passando o parametro, exibirá o parametro informado ("Alessandra")

somar_numeros(3, 2, 1)              # a=3, b=2, c=1
somar_numeros(3, 2)                 # a=3, b=2, c=0 (adotou o parametro padrao "0")
somar_numeros(b=2, c=1)             # a=0 (adotou o parametro padrao "0"), b=2, c=1
somar_numeros()                     # a=0, b=0, c=0 (adotou o parametro padrao "0" para todos os argumentos ausentes)


'''
2. Funções com RETURN (com retorno de parametros/valores)''' 

# Exemplo 1: retorna parametro único
def calcular_total(numeros):                        # Declarando a função
    soma = sum(numeros)                             
    return soma                                     # Definindo o retorno


soma = calcular_total([10, 20, 34])                 # Chamando a função
print(f'A somas dos valores é: {soma}')


# Exemplo 2: com retorno multiplo de parametros
def retorna_antecessor_sucessor(numero):            # Declarando a função
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor                     # Definindo o retorno


numero = 10
lista = retorna_antecessor_sucessor(numero)         # Chamando a função
print(f'O antecessor de {numero} é o {lista[0]}, e o sucessor é o {lista[1]}')


# Exemplo 3: com retorno condicional, booleano:
def valida_par(numero=0):
    if numero % 2 ==00:
        return True
    else:
        return False


numero = int(input('Insira o numero: '))
if valida_par(numero):
    print('O numero é par')
else:
    print('O numero é impar')



'''Exemplo 4: Função de Fatorial com Recursividade
Crie um programa que tenha uma função chamada fatorial() que receba um número inteiro como parâmetro e retorne o seu fatorial. 
A função deve ser recursiva. Não usar biblioteca math'''

def calculo_fatorial(numero=1):
    fator = 1
    for contador in range (numero, 0, -1):
        fator *= contador
    return fator


numero = int(input('Insira o numero a ser calculado: '))
print(f'O fatorial de {numero} é igual a {calculo_fatorial(numero)}')
