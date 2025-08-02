
'''Instruções Auxiliares: BREAK, CONTINUE e PASS

Declarações BREAK, CONTINUE e PASS.
Funcionam com estruturas FOR e WHILE.

1. BREAK:

É utilizada para interromper as repetições dos laços FOR e WHILE. 
Quando o programa encontra uma instrução break, a repetição é encerrada e o fluxo do programa continua a partir da primeira instrução após o laço.
'''

# 1.1. Exemplo com FOR:

for num in range(1, 11):
    if num == 5:
        break                                       # BREAK encerra o laço quando a condição é atendida (1, 2, 3, 4).
    else:
        print(num, end=', ')
print('\nLaço encerrado')


# 1.2. Exemplos Estrutura WHILE, com laço em loop do TRUE, e parada com BREAK:
 
while True:
    numero = int(input("Informe um número: ")) 
    if numero == 10:
        break                                       # BREAK encerra o laço em loop, quando a condição é atendida.
    print(numero)


while True:
   print('laço em loop')
   palavra = input('Entre com uma palavra:')
   if palavra == 'sair':
      break
print('Você digitou sair e agora está fora do laço')


# 1.3. Exemplo com BREAK em laços aninhados:

while True:
    print('Você está no primeiro laço.')
    opcao1 = input('Deseja sair dele? Digite SIM para isso. \n')
    if opcao1 == 'SIM':
        break                                       # este break é do primeiro laço: ao parar, encerra o laço.
    else:
        while True:
            print('Você está no segundo laço.')
            opcao2 = input('Deseja sair dele? Digite SIM para isso. \n')
            if opcao2 == 'SIM':
               break                                # este break é do segundo laço: ao parar, volta para o 1o laço.
        print('Você saiu do segundo laço.')
print('Você saiu do primeiro laço')


'''
2. A instrução CONTINUE:

É usada para pular a iteração atual de um laço e passar para a próxima iteração. 
Diferente do BREAK (encerra completamente o laço), a instrução CONTINUE interrompe apenas a iteração corrente e continua o laço desde o início.

Quando o Python encontra a instrução CONTINUE, ele ignora todas as instruções no laço, restantes para aquela iteração, e vai direto para a próxima iteração. 
Isso é útil quando você deseja pular certos valores ou condições dentro de um laço.
'''

# 2.1. Exemplo com FOR:

for num in range(1, 11):
    if num == 5:
        continue                                    # Pula o numero 5
    else:                                           
        print(num)                                  # 1, 2, 3, 4, 6, 7, 8, 9, 10 
print('Laço encerrado')


# 2.2. Exemplo com WHILE:


'''
3. Instrução PASS:

É usada como um marcador de posição. 
Ela é útil quando você precisa de uma sintaxe que exige um bloco de código, mas você ainda não decidiu o que escrever nesse bloco. 
Em outras palavras, PASS permite que você escreva uma estrutura que não faz nada, mas mantém a sintaxe correta.
Quando o Python encontra a instrução PASS, ele simplesmente continua a execução sem fazer nada. 
'''

# 3.1. Exemplo com PASS: 

for num in range(1, 11):      
    if num % 2 == 0:
        pass                            # PASS 'pula' os números pares.
    else:
        print(num)                      # Exibe somente os números ímpares entre 1 e 10. 
print('Laço encerrado')

