'''
Aula 012: Estrutura Condicional Aninhada
if / elif / else

Aula 013: Estrutura em laço de repetição
for / in
'''

for numero in range(1, 8, -1):      #mostra o último
    print(numero)
    print('Oi')
print('fim do intervalo', '\n')


for numero in range(1, 8):          #mostra todos
    print(numero+1)
    print('Oi')
print('fim do intervalo', '\n')


inicio = 0                          #inicio do range
fim = 8                             #final do range (não entra)
intervalo = 2

for numero in range(inicio, fim + 1, intervalo): #pula intervalo
    print(numero)
    print('Par')
print('fim do intervalo', '\n')


for repeticao in range(0, 3):          #repete 3x (3-0)
    numero = int(input('Digite um numero: '))
    print('Errou!', '\n')
print('Fim das tentativas', '\n')


soma = 0

for repeticao in range(0, 3):          #repete 3x (3-0)
    numero = int(input('Digite um numero: '))
    soma += numero
    print(f'Somatório agora é: {soma} ', '\n')
print('Fim das tentativas', '\n')
