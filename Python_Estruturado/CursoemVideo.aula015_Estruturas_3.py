'''
Aula 013 - Estruturas de laços de repetição 1
           Variáveis de Controle
for / in: precisa de limites claros de inicio e fim

Aula 014 - Estruturas de laços de repetição 2
           Repetição com teste lógico
while: repete até alcançar a condição (obrigatória)

Aula 015 - Estruturas de laços de repetição 3
           Repetição com ponto de interrupçao
while True: loop infinito
break: interrompe a execuçao
'''

numero = soma = 0
while True:
    numero = int(input('Digite um numero: '))
    if numero == 999:
        break
    soma += numero
print(f'A soma vale {soma}.')