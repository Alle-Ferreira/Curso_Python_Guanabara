def aumentar(numero, incremento, formatar=False):
    resultado = numero + incremento
    return formatar_moeda(resultado) if formatar else resultado


def diminuir(numero, redutor, formatar=False):
    resultado = numero - redutor
    return formatar_moeda(resultado) if formatar else resultado


def dobrar(numero, formatar=False):
    resultado = numero * 2
    return formatar_moeda(resultado) if formatar else resultado


def dividir_2(numero, formatar=False):
    resultado = numero / 2
    return formatar_moeda(resultado) if formatar else resultado


def formatar_moeda(numero, moeda='R$'):
    return f'{moeda} {numero:,.2f}'.replace(',', 'v').replace('.', ',').replace('v', '.')

''' Passo a passo da função formatar_moeda
def formatar_moeda(numero, moeda='R$'):
    valor_formatado = f'{numero:,.2f}'              # Ex: '1,234.56' (estilo americano)
    passo1 = valor_formatado.replace(',', 'v')      # Troca vírgulas por 'v': '1v234.56'
    passo2 = passo1.replace('.', ',')               # Troca ponto decimal por vírgula: '1v234,56'
    passo3 = passo2.replace('v', '.')               # Troca 'v' por ponto: '1.234,56'
    resultado = f'{moeda} {passo3}'                 # Adiciona símbolo de moeda: 'R$ 1.234,56'
    return resultado'''

def exibir_resumo(numero, fator, formatar=False):
    valor = formatar_moeda(numero) if formatar else numero
    print('-' * 40)
    print('RESUMO DO VALOR'.center(40))
    print('-' * 40)
    print(f'{"Valor analisado:":<25}{formatar_moeda(numero):>15}')
    print(f'{"Dobro do preço:":<25}{dobrar(numero, formatar=True):>15}')
    print(f'{"Metade do preço:":<25}{dividir_2(numero, formatar=True):>15}')
    # f-strings aninhadas nas linhas 41 e 42:
    print(f'{f"{fator:.2f} de aumento:":<25}{aumentar(numero, fator, formatar=True):>15}') 
    print(f'{f"{fator:.2f} de redução:":<25}{diminuir(numero, fator, formatar=True):>15}')
    print('-' * 40)
