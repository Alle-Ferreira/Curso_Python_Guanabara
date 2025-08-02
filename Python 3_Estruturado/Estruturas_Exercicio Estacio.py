'''Estruturas de decisão e repetição na prática

Atividade 4:

Faça um programa em Python que:

a) Mostre os números entre 1000 e 9999,
   b) Cuja raiz quadrada seja igual à:
        c) soma dos números formados pelos:
            d) dois algarismos menos significativos e 
            e) pelos dois algarismos mais significativos. 

Roteiro:
- Utilize uma estrutura de for para gerar os números a serem testados.
- Gere o número formado pelos algarismos menos significativos.
- Gere o número formado pelos algarismos mais significativos.
- Obtenha a raiz somando os dois números obtidos.
- Eleve a raiz ao quadrado e valide se é igual ao número que está sendo testado.
- Se for igual, exiba:
    o número que está sendo testado, 
    os números dos algarismos mais e menos significativos,
    e a raiz.
- Ao término do loop, informe que terminou e mostre o valor final da variável do for.
- Existem três números que atendem a condição.

Informação posterior:
Os algarismos menos significativos são aqueles que têm menos peso na representação de um número. 
São, geralmente, os algarismos mais à direita em um número inteiro ou após a vírgula num número decimal. 

numero menos significativo: menor = num % 100   (dois últimos dígitos)
numero mais significativo: maior = num // 100   (dois primeiros dígitos)
'''

for numero in range (1000, 10000):      # a)
    maior = numero // 100               # e)
    menor = numero % 100                # d)
    raiz = menor + maior                # c)

    if (raiz * raiz) == numero:         # b)
        print(numero)
        print(menor)
        print(maior)
        print(raiz)
print('terminou')
print('saiu', numero)




'''
Atividade 5

A solução apresentada inicialmente no vídeo prático é eficaz, mas não é a mais eficiente, já que ela testa todos os números entre 1000 e 9999.

Foi observado no vídeo uma característica especial, que é o fato de a raiz ser obrigatoriamente um número inteiro, já que ela irá resultar da soma de dois números inteiros.

A otimização demonstrada no vídeo foi diminuir o loop para testar apenas as raízes inteiras de 32 a 99, que geram números entre 1000 e 9999:
- O valor 32 representa o menor número que tem uma raiz inteira e cujo quadrado está no intervalo de 1000 a 9999. 
- Já o valor 99 representa o maior número que tem uma raiz inteira e cujo quadrado está no intervalo citado.

Altere então o programa apresentado inicialmente no vídeo prático, de modo que os valores 32 e 99 da otimização possam ser obtidos de maneira automática, sem nenhum cálculo anterior à execução do programa.
'''

# Sintaxe 1: 

import math

nr_inicio = math.sqrt(1000)
nr_final = math.sqrt(9999)

for raiz in range(nr_inicio, nr_final + 1):
    numero = raiz * raiz
    maior = numero // 100               
    menor = numero % 100 

if maior + menor == numero:         
        print(numero)
        print(maior)
        print(menor)
        print(raiz)
print('terminou')
print('saiu', numero)


# Sintaxe 2: 

start = int(1000**0.5) # Aproximação da raiz quadrada de 1000

if start * start < 1000: 
	start += 1 # Ajusta para garantir que o quadrado seja pelo menos 1000 

end = int(9999**0.5) # Aproximação da raiz quadrada de 9999 

for raiz in range (start, end + 1): 
	num = raiz * raiz  #calcula o numero gerado pela raiz
	menor = num % 100  #obtem o numero dos algarismos menos significativos
	maior = num // 100  #obtem o numero dos algarismos mais significativos
 
	if (menor +maior) ==raiz:  #valida se a raiz corresponde a soma
		print(num)
		print(menor)
		print(maior)
		print(raiz)
print('terminou')
print('saiu ', raiz) 