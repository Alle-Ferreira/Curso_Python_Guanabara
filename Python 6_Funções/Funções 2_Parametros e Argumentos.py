'''
Subprogramas: Argumentos e Parametros em funções

a) Parametros formais: nome das variaveis a serem descritas na função.
b) Parametros reais: sao os valores reais, referentes a cada variavel, passados para a execução do sub-programa.


1. Argumento Nomeado: chave-valor

a) Declarando a função:'''

def salvar_carro(marca, modelo, ano, placa):                                           
    print(f'Carro {marca}/{modelo} {ano}, com placa {placa}, inserido com sucesso.')


'''
b) Chamando a função: 
   - Usualmente é feita dentro do programa principal
   - Pode ser feita dentro de outra função'''

salvar_carro('Fiat', 'Palio', 1999, 'ABC-1234')                                         
#Desvantagem: se inverter a ordem, mostrará no campo errado.

salvar_carro(marca='Fiat', modelo='Palio', ano=1999, placa='ABC-1234')

salvar_carro(**{'marca': 'Fiat', 'modelo': 'Palio', 'ano': 1999, 'placa': 'ABC-1234'})  
#Neste formato de dicionário, ele vai procurar pelas palavras-chave, e aplicar como parametro.


'''
2. Argumentos múltiplos: Args (arguments) e Kwargs (key_arguments)

    # Args      (*)     posicional      Tuplas
    # Kwargs    (**)    chave_valor     Dicionarios

    
# Exemplo 1:'''

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = '\n'.join([f'{chave.title()}: {valor}' for chave, valor in kwargs.items()])
    mensagem = f'{data_extenso}\n\n{texto}\n\n{meta_dados}'
    print(mensagem)


# Programa Principal
exibir_poema(
    'Domingo, 30 de março de 2025',         # data_extenso
    'Zen of Python',                        # *args
    'Beautiful is better than ugly.',       # *args
    autor='Tim Peters',                     # **kwargs
    ano=1999)                               # **kwargs


'''
2.1. Função com parametros múltiplos em uma lista []:

- Não há necessidade de desempacotar a lista.
- Como a lista é mutável, os valores também podem ser alterados dentro da função e retornados.

Exemplo 1:'''

def multiplicapor2(lista):
    posicao = 0
    while posicao < len(lista):
        lista[posicao] *= 2
        posicao += 1
    print(lista)


# Programa Principal
multiplicapor2([1, 2, 3])

lista = [1, 2, 3, 4, 5]
multiplicapor2(lista)


'''
Exemplo 2: Estacio Módulo 2 - Atividade 3

Escreva uma função que busca de forma iterativa o maior elemento em uma lista de números inteiros.
Encontrar o maior elemento em uma lista de números inteiros de forma não recursiva.
- Args: a lista de números inteiros.
- Returns: o maior elemento da lista.
'''

def encontrar_maior_elemento_iterativo(lista):

  if len(lista) <= 1:                    # Caso base: se a lista tiver no máximo 1 elemento, ele é o maior
    return lista[0]

  maior_elemento = lista[0]
  for numero in lista[1:]:
    if numero > maior_elemento:
      maior_elemento = numero

  return maior_elemento


# Programa Principal
lista_exemplo = [7, 2, 5, 1, 4, 3, 6]

maior_elemento = encontrar_maior_elemento_iterativo(lista_exemplo)
print(f"O maior elemento da lista é: {maior_elemento}")

'''
2.2. Função com parametros múltiplos em uma Tupla(): operador "*"

Quando parametros em uma tupla são passados para uma função, é necessário usar o operador "*" para desempacotar a tupla.
Dentro da função, os parametros são tratados como uma tupla: serão imutaveias.
'''

def soma(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    print(f"A soma é: {total}")
    print()


# Programa Principal
soma(1, 2, 3)               # chamada com envio dos dados da Tupla não precisa do operador

tupla = (4, 5, 6, 7, 8)
soma(*tupla)                # chamada pelo nome da tupla necessita do operador * para desempacotar parametros.

