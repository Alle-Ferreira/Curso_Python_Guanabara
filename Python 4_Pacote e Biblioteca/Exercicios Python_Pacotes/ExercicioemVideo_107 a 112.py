#from funcoes_uteis import moeda, validacao_entradas

#numero = validacao_entradas.ler_int('Digite um numero inteiro: ')
#fator = 20

from utilidadesCeV import moeda, entradas

numero = entradas.ler_int('Digite um numero inteiro: ')
fator = 20

'''Exercício Python 107 - Exercitando módulos em Python
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). 
Faça também um programa que importe esse módulo e use algumas dessas funções.'''

aumento = moeda.aumentar(numero, fator)
reducao = moeda.diminuir(numero, fator)
dobro = moeda.dobrar(numero)
metade = moeda.dividir_2(numero)

print(f'{numero:.2f} com o incremento de {fator:.2f} é igual a {aumento:.2f}.')
print(f'{numero:.2f} com a redução de {fator:.2f} é igual a {reducao:.2f}.')
print(f'O dobro de {numero:.2f} é {dobro:.2f}.')
print(f'A metade de {numero:.2f} é {metade:.2f}.')
print()


'''Exercício Python 108 - Formatando Moedas em Python
Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.'''

numero_formatado = moeda.formatar_moeda(numero, 'R$')
print(f'O valor em questão é {numero_formatado}.')
print()


'''Exercício Python 109 - Formatando Moedas em Python
Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.'''

print(f'Resultado aumento: {moeda.aumentar(numero, fator, formatar=True)}')
print(f'Resultado redução: {moeda.diminuir(numero, fator, formatar=True)}') 
print(f'Resultado dobro: {moeda.dobrar(numero, formatar=True)}')            
print(f'Resultado metade: {moeda.dividir_2(numero, formatar=True)}')
print()


'''Exercício Python 110 - Reduzindo ainda mais seu programa
Adicione ao módulo moeda.py, criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.'''

resumo = moeda.exibir_resumo(numero, fator, formatar=True)
print()


'''Exercício Python 111 - Transformando módulos em pacotes
Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.'''

# módulos e pacote criados. 

'''Exercício Python 112 - Entrada de entradas monetários
Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada ler_Dinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de entradas para aceitar apenas valores que sejam monetários.'''

numero = entradas.ler_moeda('Digite o valor principal: R$ ')
fator = entradas.ler_moeda('Digite o valor do ajuste: R$ ')

moeda.exibir_resumo(numero, fator, formatar=True)
