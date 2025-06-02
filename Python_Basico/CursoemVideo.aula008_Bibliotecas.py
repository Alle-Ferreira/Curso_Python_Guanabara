# Bibliotecas Python

'''
1. Math:
Vem instalado, precisa apenas importar.

.ceil(): arredonda numero para cima
.floor(): arredonda numero para baixo
.trunc(): exclui casas decimais             # truncate 
.pow (): calcula a potencia                 # power
.sqrt(): calcula raiz quadrada              # square root
.factorial(): calculo de fatoriais

Sintaxe de Importação:

a) Importando toda a biblioteca: precisa referenciar a biblioteca no codigo.     
'''
import math    
         
numero = int(input('Informe um numero: '))
raiz_quadrada = math.sqrt(numero)
print(raiz_quadrada)
print()

'''
b)  Importando classe(s) específicas da biblioteca: não precisa referenciar.
'''
from math import sqrt, trunc    

numero = int(input('Informe outro numero: '))
raiz_quadrada = sqrt(numero)
print(trunc(raiz_quadrada))
print()


'''
2. Random
Vem instalado, precisa apenas importar.

.random(): numero randomico entre 0 e 1
.randint(): numero randomico inteiro, dentro do intervalo definido.
.randrange(): gera um número inteiro aleatório a partir de uma intervalo específico.
              aceita start, stop e step
'''
import random

numero = random.random()
print(numero)
print()

numero1 = random.randint(1, 50)   # numero entre o 1 na posição (0) e o 50 posição (49).
print(numero1)
print()

numero2 = random.randrange(1,150,2)  # numero entre posição 1 (0) à posição 150 (149), pulando de 2 em 2 numeros.
print(numero2)
print()

'''
3. Datetime
Vem instalado, precisa apenas importar.

date():                            aa/mm/dd
time():                            00:00:00
datetime():                        aa/mm/dd 00:00:00

date.today(): data atual
datetime.today(): data e horario atuais


4. Emoji
É uma biblioteca 'externa': nao vem instalada no Python, então primeiro precisa instalar.

(Olhar na documentação do Python)
'''