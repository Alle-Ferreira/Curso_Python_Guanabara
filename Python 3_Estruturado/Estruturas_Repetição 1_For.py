''' Estruturas de Repetição: FOR e RANGE

1. Estrutura de Repetição FOR:

- Usadas para repetir determinados trechos do código determinadas vezes.
- O numero de vezes pode ser pre-determinado ou derivado de uma expressão logica.
- FOR é usado quando o numero de repetições é pre-determinado, ou quando queremos percorrer um objeto iterável (string).
- A estrutura for tem a seguinte sintaxe em Python:

for <variável> in <sequência>:
     Bloco que será repetido para todos os itens da sequência
Instrução fora do for

- A variável recebe o valor de cada item da sequência a cada iteração.
- A sequência pode ser uma lista, tupla, string, dicionário ou qualquer objeto iterável.
'''
# Exemplos de FOR percorrendo um objeto iterável (string):

nome = input("Entre com seu nome: \n")
for letra in nome:
    print(letra, end=', ')                      # END força a listar na mesma linha


texto = input('Informe seu trecho de livro favorito: ')
VOGAIS = 'AEIOU'                                # VOGAIS: lista não mutavel
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")                        
print('\nfim')


texto = "programação"
letra_para_contar = "a"
contador = 0
for letra in texto:
    if letra == letra_para_contar:
        contador += 1
print(f"A letra '{letra_para_contar}' aparece {contador} vezes na palavra '{texto}'.")


''' 
2. Estrutura de função Built-in RANGE

- Usada para gerar uma sequência de números inteiros.
- Inicio do range é inclusivo
- Fim do range é exclusivo'''

# Exemplo de sintaxe simples:
range (4)                                       # range(0,4): sequencia de números de 0 a 3 (0,1,2,3)

# Exemplos de sintaxe com argumentos:
range(1, 10)                                    # sequencia de números de 1 a 9 (1,2,3,4,5,6,7,8,9)
list(range(4))                                  # cria a lista [0,1,2,3]
list(range(10,15))                              # cria a lista [10,11,12,13,14]

# Exemplo sintaxe indicando início, fim e passo:
# Recebe 3 argumentos:
    #stop (obrigatorio)
    #start (opcional)
    #step (opcional)
range(2, 9, 3)                                  # Cria a sequência (2, 5, 8)

# Tabuada simples - Exemplo de FOR percorrendo uma sequencia
numero_entrada = 5                                  
for multiplicador in range(1, 11):              # sequencia de 1 a 10
    resultado = numero_entrada * multiplicador
    print(f'{numero_entrada} x {multiplicador} = {resultado}')


'''
3. Estrutura FOR com a função Built-in RANGE

- Usada para repetir determinados trechos do código determinadas vezes.
- O numero de vezes pode ser pre-determinado ou derivado de uma expressão logica.
- Argumentos: START, STOP e STEP.
'''

# Exemplo 1 - Argumentos START e STOP
for numero in range(0,11):                      
    print(numero, end="")                       # END força a listar na mesma linha
else:
    print()

# Exemplo 2 - Argumentos START, STOP e STEP
for numero in range(0, 51, 5):               
    print(numero, end="")
else:
    print()


'''
4. FOR em listas
O FOR pode ser empregado para percorrer uma lista.

Lista é uma coleção de elementos que pode conter itens de diferentes tipos.
Listas são mutáveis, o que significa que seus elementos podem ser alterados após a criação. 
Elas são definidas usando colchetes [ ] e os elementos são separados por vírgulas.
'''
nomes = ['Laura', 'Lis', 'Guilherme', 'Enzo', 'Arthur']
numeros = [1, 2, 3, 4, 5]

for nome in nomes:
    print(nome)


busca_nome = input('Informe o nome a ser verificado: ')     # Diferencia maiúsculas de mínusculas: necessita tratamento
for nome in nomes:
    if nome == busca_nome:                              
        print(f'Sim, {nome} está na lista')


soma = 0
for numero in numeros:
    soma += numero
print(f'A soma de todos os números é {soma}')


for numero in numeros:
    quadrado = numero ** 2
    print(f'O quadrado de {numero} é {quadrado}')