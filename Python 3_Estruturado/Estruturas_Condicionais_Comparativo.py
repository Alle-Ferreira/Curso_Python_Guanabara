# Estruturas Condicionais

#IF: estrutura condicional simples, composta por UNICO desvio

#IF / ELSE: estrutura condicional composta por DOIS desvios
    #Se a expessão testada no IF for verdadeira, o bloco de codigo do IF será executado
    #Se a expessão testada no IF for falsa, o bloco de codigo do ELSE será executado

#IF / ELIF / ELSE: estrutura condicional composta por MAIS DE DOIS desvios
    #O ELIF pode se repetir quantas vezes forem necessárias para testar as condições

MAIOR_IDADE = 18
MSG_VERIFICAO = 'Informe sua idade, por favor: '
MSG_SUCESSO = 'Voce já tem a idade mínima para fazer sua CNH!'
MSG_MENOR = 'Voce não tem ainda a idade mínima para fazer sua CNH!'
MSG_17ANOS = 'Falta pouco tempo para a sua maior idade! Você já pode começar sua preparação.'
MSG_17ANOS_6M = 'Quantos meses faltam para o seu próximo aniversário? '
MSG_ESCOLAS = 'Na opção ESCOLAS você poderá visualizar escolas credenciadas, para fazer suas aulas práticas.'
MSG_MATERIAL = 'Clicando em MATERIAL, você poderá baixar apostila e legislação, e estudar para a prova escrita. Boa sorte!'
MSG_FUTURO = 'Ainda falta algum tempo...vejo você no futuro!'

#Exemplo de código 1: usando IF
print('Exercicio_1: IF')
idade = int(input(MSG_VERIFICAO))
if idade >= MAIOR_IDADE:
    print(MSG_SUCESSO)
    print(MSG_ESCOLAS)
    print(MSG_MATERIAL)
    print()
if idade < MAIOR_IDADE:
    print(MSG_MENOR)
    print()

#Exemplo mesmo código 2: usando IF/ELSE   
print('Exercicio_2: IF/ELSE')
idade = int(input(MSG_VERIFICAO))
if idade >= MAIOR_IDADE:
    print(MSG_SUCESSO)
    print(MSG_ESCOLAS)
    print(MSG_MATERIAL)
    print()
else:
    print(MSG_MENOR)
    print()
     
#Exemplo mesmo código 3: usando IF/ELIF/ELSE
print('Exercicio_3: IF/ELIF/ELSE')
idade = int(input(MSG_VERIFICAO))
if idade >= MAIOR_IDADE:
    print(MSG_SUCESSO)
    print(MSG_ESCOLAS)
    print(MSG_MATERIAL)
    print()
elif idade == 17:
    meses = int(input(MSG_17ANOS_6M))
    if meses <= 6:
        print(MSG_17ANOS)
        print(MSG_MATERIAL)
        print()
    else:
        print(MSG_MENOR)
        print(MSG_FUTURO)
        print()
else:
    print(MSG_MENOR)
    print(MSG_FUTURO)
    print()

    