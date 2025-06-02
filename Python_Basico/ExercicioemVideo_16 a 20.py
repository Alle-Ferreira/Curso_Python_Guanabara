'''
Desafio 016:
Desenvolva um programa que leia um número real inserido, 
e exiba a sua porção inteira.
'''

numero_real = float(input('Digite um numero: '))

# Sintaxe 1:
from math import trunc
print(f'O número digitado foi {numero_real}, e sua porção inteira é {trunc(numero_real)}.')

# Sintaxe 2:
print(f'O número digitado foi {numero_real}, e sua porção inteira é {int(numero_real)}.')
print()


'''
Desafio 017:
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
- triangulo retangulo: angulo de 90 graus
- quadrado da hipotenusa = soma dos quadrados dos catetos
'''

cateto_oposto = float(input('Informe o tamanho do cateto oposto, em metros: '))
cateto_adjacente = float(input('Informe o tamanho do cateto adjacente, em metros: '))

# Sintaxe 1:
hipotenusa = ((cateto_oposto**2) + (cateto_adjacente**2)) ** (1/2)
print(f'O comprimento da hipotenusa é {hipotenusa:.2f}')

# Sintaxe 2:
from math import sqrt
hipotenusa = sqrt((cateto_oposto**2) + (cateto_adjacente**2))
print(f'O comprimento da hipotenusa é {hipotenusa:.2f}')

# Sintaxe 3:
from math import hypot
hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print(f'O comprimento da hipotenusa é {hipotenusa:.2f}')
print()


'''
Desafio 018:
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

Métodos da classe Math:
. seno/sen (eixo vertical): método .sin()
. cosseno/cos (eixo horizontal): método .cos()
. tangente/tan: método .tan()
. radians(): converte um angulo de graus para radianos.
. degrees(): converte um angulo de radianos para graus.
'''

angulo = float(input('Informe o angulo do telhado: '))

from math import sin, radians, cos, tan

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f'''O angulo de {angulo:.2f} graus tem seno de {seno:.2f}, 
tem cosseno de {cosseno:.2f}, e tangente de {tangente:.2f}.
''')
print()


'''
Desafio 019:
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

Método da classe Random: 
. choice(): retorna um elemento aleatório da sequência não vazia.
            Se seq estiver vazio, levanta IndexError.
'''
aluno1 = input('Insira o nome do primeiro aluno da lista: ')
aluno2 = input('Insira o nome do próximo aluno da lista: ')
aluno3 = input('Insira o nome do próximo aluno da lista: ')
aluno4 = input('Insira o nome do próximo aluno da lista: ')
alunos = [aluno1, aluno2, aluno3, aluno4]

from random import choice
escolhido = choice(alunos)

print(f'O aluno escolhido para apagar o quadro é {escolhido}')
print()


'''
Desafio 020:
O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. 
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

Método da classe Random: 
. shuffle(): Embaralha a sequência internamente.

'''

alunos = ['Alexandre', 'Alice', 'Gleisson', 'Raquel']

from random import shuffle
shuffle(alunos)

print(f'A ordem de apresentação será {alunos}')
print()