numeros = (                                                     # Tupla com os números por extenso de 0 a 20
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco',
    'seis', 'sete', 'oito', 'nove', 'dez',
    'onze', 'doze', 'treze', 'quatorze', 'quinze',
    'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
)
while True:                                                     # Validação: só aceitar números entre 0 e 20
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        print(f'Você digitou o número {numeros[n]}.\n')                   # Exibir o número por extenso
        break
    print('Número inválido! Tente novamente.')