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
# Exemplo de Uso:

# Caso 1 - sem loop infinito

count = 0
soma = 0
numero = 0

while numero != 999:
    numero = int(input('Digite um numero: '))
    if numero == 999:
        break
    count += 1
    soma += numero
print(f'Você digitou {count} números e a soma deles é {soma}.\n')


# Caso 2 - com loop infinito

contador = 0
somatorio = 0

while True:
    numero1 = int(input('Digite um numero'))
    if numero1 == 999:
        break
    contador += 1
    somatorio += numero1
print(f'Você digitou {contador} números e a soma deles é {somatorio}.')